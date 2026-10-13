#!/usr/bin/env python3
"""STOCKS corporate action verifier: local evidence registry + web discovery."""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
VERIFY_DIR = ROOT / "AÇÕES" / "VERIFICADOR_EVENTOS_SOCIETARIOS"
REGISTRY_FILES = {
    "GRUPAMENTO": ROOT / "AÇÕES" / "GRUPAMENTOS" / "registros.json",
    "DESDOBRAMENTO": ROOT / "AÇÕES" / "DESDOBRAMENTOS" / "registros.json",
    "BONIFICACAO": ROOT / "AÇÕES" / "BONIFICACOES" / "registros.json",
}
OFFICIAL_HINTS = ("b3.com.br", "gov.br/cvm", "investidor", "ri.", "ri/")
SEARCH_URL = "https://html.duckduckgo.com/html/?q="


class SearchResultParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.results: list[dict[str, str]] = []
        self._capture = False
        self._href = ""
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag == "a" and "result__a" in (attr.get("class") or ""):
            self._capture = True
            self._href = attr.get("href") or ""
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._capture:
            title = " ".join(" ".join(self._text).split())
            url = self._normalise_result_url(self._href)
            if title and url:
                self.results.append({"title": title, "url": url})
            self._capture = False
            self._href = ""
            self._text = []

    @staticmethod
    def _normalise_result_url(value: str) -> str:
        if not value:
            return ""
        parsed = urllib.parse.urlparse(html.unescape(value))
        if parsed.hostname and parsed.hostname.endswith("duckduckgo.com") and parsed.path == "/l/":
            target = urllib.parse.parse_qs(parsed.query).get("uddg", [""])[0]
            return target
        return html.unescape(value)


def search_web(ticker: str, timeout: int = 12) -> tuple[list[dict[str, str]], list[str]]:
    """Discover pages only; search snippets never count as verified evidence."""
    queries = [
        f'"{ticker}" grupamento ações',
        f'"{ticker}" desdobramento ações split',
        f'"{ticker}" bonificação ações',
        f'"{ticker}" site:b3.com.br grupamento OR desdobramento',
        f'"{ticker}" site:gov.br/cvm grupamento OR desdobramento',
        f'"{ticker}" site:ri.* desdobramento OR grupamento',
    ]
    found: list[dict[str, str]] = []
    errors: list[str] = []
    seen: set[str] = set()
    for query in queries:
        url = SEARCH_URL + urllib.parse.quote(query)
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "STOCKS-CorporateActionVerifier/1.0 (research; contact via repository issues)"},
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                page = response.read(2_000_000).decode("utf-8", errors="replace")
            parser = SearchResultParser()
            parser.feed(page)
            for item in parser.results:
                if item["url"] not in seen:
                    seen.add(item["url"])
                    item["query"] = query
                    item["official_hint"] = any(hint in item["url"].lower() for hint in OFFICIAL_HINTS)
                    found.append(item)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            errors.append(f'{query}: {exc.__class__.__name__}: {exc}')
    return found, errors


def load_events() -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    errors: list[str] = []
    for expected_type, path in REGISTRY_FILES.items():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            for event in payload.get("events", []):
                if event.get("event_type") != expected_type:
                    errors.append(f"{path}: tipo de evento incompatível em {event.get('event_id', 'sem ID')}")
                    continue
                events.append(event)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: {exc}")
    return events, errors


def validate_verified_event(event: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    required = ("event_id", "ticker", "event_type", "post_event_shares_per_pre_event_share",
                "effective_date", "source_url", "source_type", "verification_status")
    for key in required:
        if event.get(key) in (None, ""):
            problems.append(f"campo obrigatório ausente: {key}")
    factor = event.get("post_event_shares_per_pre_event_share")
    if not isinstance(factor, (int, float)) or isinstance(factor, bool) or factor <= 0:
        problems.append("post_event_shares_per_pre_event_share tem de ser um número positivo")
    elif event.get("event_type") == "GRUPAMENTO" and factor >= 1:
        problems.append("grupamento exige fator inferior a 1 (ações novas por ação antiga)")
    elif event.get("event_type") == "DESDOBRAMENTO" and factor <= 1:
        problems.append("desdobramento exige fator superior a 1 (ações novas por ação antiga)")
    elif event.get("event_type") == "BONIFICACAO" and factor <= 1:
        problems.append("bonificação exige fator total superior a 1 (ações após / ações antes)")
    if event.get("verification_status") == "VERIFICADO":
        if event.get("source_type") not in {"RI_EMISSOR", "B3", "CVM"}:
            problems.append("evento VERIFICADO exige fonte primária RI_EMISSOR, B3 ou CVM")
        if not event.get("verified_by") or not event.get("verified_at"):
            problems.append("evento VERIFICADO exige verified_by e verified_at")
        if not str(event.get("source_url", "")).startswith("https://"):
            problems.append("evento VERIFICADO exige URL HTTPS")
    return problems


def build_report(ticker: str, events: list[dict[str, Any]], candidates: list[dict[str, str]],
                 search_errors: list[str], registry_errors: list[str], offline: bool) -> tuple[str, str]:
    matches = [event for event in events if str(event.get("ticker", "")).upper() == ticker]
    verified = [event for event in matches if event.get("verification_status") == "VERIFICADO"]
    pending = [event for event in matches if event.get("verification_status") == "PENDENTE"]
    invalid: list[tuple[dict[str, Any], list[str]]] = []
    for event in verified:
        problems = validate_verified_event(event)
        if problems:
            invalid.append((event, problems))

    if invalid or registry_errors:
        status = "FAIL"
    elif pending or candidates or search_errors:
        status = "WARN"
    elif verified:
        status = "PASS"
    else:
        status = "UNKNOWN"

    lines = [
        f"# Verificação de eventos societários — {ticker}", "",
        f"- **Estado:** {status}",
        f"- **Data/hora UTC:** {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- **Modo:** {'offline' if offline else 'online (descoberta de candidatos)'}",
        "- **Limite de cobertura:** este relatório não prova inexistência de eventos quando não encontra evidência.",
        "", "## Eventos no registo local", ""
    ]
    if matches:
        for event in matches:
            lines += [
                f"### {event.get('event_id', 'Evento sem ID')} — {event.get('event_type', 'tipo desconhecido')}",
                f"- Estado de verificação: {event.get('verification_status', 'UNKNOWN')}",
                f"- Fator (ações novas por ação antiga): {event.get('post_event_shares_per_pre_event_share', 'ND')}",
                f"- Data efetiva: {event.get('effective_date', 'ND')}",
                f"- Fonte: {event.get('source_url', 'ND')}",
                f"- Tipo de fonte: {event.get('source_type', 'ND')}",
                f"- Revisor: {event.get('verified_by') or 'ND'}",
                f"- Notas: {event.get('notes') or 'ND'}", ""
            ]
    else:
        lines.append("Nenhum evento registado para este ticker. Isso **não** significa que nunca tenha ocorrido evento.")
        lines.append("")

    lines += ["## Candidatos encontrados na pesquisa web", ""]
    if candidates:
        for item in candidates:
            label = "possível fonte primária" if item.get("official_hint") else "fonte a avaliar"
            lines.append(f"- [{item['title']}]({item['url']}) — {label}; consulta: {item.get('query', '')}")
    elif not offline:
        lines.append("Não foram extraídos candidatos. O motor de pesquisa pode ter bloqueado a consulta ou não ter devolvido resultados.")
    else:
        lines.append("Pesquisa web desativada.")
    lines += ["", "## Erros / limitações", ""]
    all_errors = registry_errors + search_errors
    if all_errors:
        lines.extend(f"- {error}" for error in all_errors)
    else:
        lines.append("- Nenhum erro técnico reportado.")
    lines += [
        "", "## Decisão e próximo passo", "",
        "- Não marcar eventos como VERIFICADOS a partir de snippets ou resultados de pesquisa.",
        "- Abrir a fonte primária, confirmar ticker/classe, proporção e datas, e adicionar o registo à pasta correspondente.",
        "- Se a pesquisa for inconclusiva, manter UNKNOWN e consultar RI, B3 e CVM.",
        "", "## Impacto na série de preços", "",
        "Para cada evento validado, usar fator = ações totais após / ações antes. Para converter um preço histórico para unidades atuais, dividir o preço pelo produto dos fatores aplicáveis após a data desse preço. Bonificação de 33,3333% corresponde a fator total aproximado de 1,333333.",
        "O preço de IPO/emissão inicial deve ser pesquisado separadamente; o histórico de grupamentos e desdobramentos não substitui a fonte do preço inicial."
    ]
    return status, "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", required=True, help="Ticker, por exemplo PETR4")
    parser.add_argument("--offline", action="store_true", help="Não consultar a internet")
    parser.add_argument("--output", help="Caminho de saída Markdown; por omissão, não grava ficheiro")
    args = parser.parse_args()
    ticker = args.ticker.strip().upper()
    if not re.fullmatch(r"[A-Z0-9]{4,12}", ticker):
        parser.error("ticker inválido; use 4–12 caracteres alfanuméricos")

    events, registry_errors = load_events()
    candidates: list[dict[str, str]] = []
    search_errors: list[str] = []
    if not args.offline:
        candidates, search_errors = search_web(ticker)
    status, report = build_report(ticker, events, candidates, search_errors, registry_errors, args.offline)

    if args.output:
        destination = Path(args.output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(report, encoding="utf-8")
    print(report)
    return 1 if status == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
