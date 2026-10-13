# Verificador de Grupamentos e Desdobramentos

**ID:** STOCKS-EVENTOS-VER-001 · **Versão:** 1.0.0 · **Estado:** MVP documental e CLI, sujeito a validação operacional.

## Objetivo
Quando um ticker for indicado para análise, executar uma verificação de eventos de grupamento e desdobramento, pesquisar referências públicas e consultar o registo local. O objetivo é identificar alterações na quantidade de ações e permitir reconciliar séries de preços.

## Pastas de dados
- `../GRUPAMENTOS/registros.json`: eventos verificados de grupamento.
- `../DESDOBRAMENTOS/registros.json`: eventos verificados de desdobramento.
- `schemas/evento-societario.schema.json`: contrato de dados.
- `scripts/verificar_eventos.py`: CLI de verificação local e descoberta web.
- `tests/test_verificar_eventos.py`: testes automatizados.
- `relatorios/`: saída de relatórios por ticker.

## Como executar
Na raiz do repositório, com Python 3.11+:

```bash
python AÇÕES/VERIFICADOR_EVENTOS_SOCIETARIOS/scripts/verificar_eventos.py --ticker PETR4
```

Para não consultar a internet:

```bash
python AÇÕES/VERIFICADOR_EVENTOS_SOCIETARIOS/scripts/verificar_eventos.py --ticker PETR4 --offline
```

Para escrever relatório num caminho específico:

```bash
python AÇÕES/VERIFICADOR_EVENTOS_SOCIETARIOS/scripts/verificar_eventos.py --ticker PETR4 --output AÇÕES/VERIFICADOR_EVENTOS_SOCIETARIOS/relatorios/PETR4.md
```

O modo online usa pesquisa pública na web para **descobrir candidatos**. A disponibilidade e estrutura do motor de pesquisa podem mudar. As páginas encontradas não são automaticamente aceites como prova de evento; os dados só passam a VERIFICADOS depois de revisão da fonte primária e registo de proporção e datas.

## Estados
- **PASS:** há evento(s) registado(s) com evidência primária e revisão preenchida; significa que os eventos registados passaram validações estruturais, não que toda a história da companhia foi provada completa.
- **WARN:** foram encontradas pistas web, falhas parciais ou eventos que aguardam revisão.
- **UNKNOWN:** a pesquisa não conseguiu estabelecer cobertura suficiente. Não significa que não existam eventos.
- **FAIL:** registo inválido, proporção incoerente ou evidência obrigatória ausente num evento marcado como verificado.

## Fórmula para normalização de preços
Para evento com `new_shares_per_old_share = fator`, o preço histórico expresso em unidades antigas é convertido para unidades atuais dividindo pelo produto dos fatores posteriores ao preço observado. Exemplo: split 5:1 → fator 5 → preço histórico dividido por 5. Grupamento 1:10 → fator 0,1 → preço histórico dividido por 0,1 (multiplicado por 10).

**Limite importante:** o preço inicial de oferta/abertura de capital (IPO) é um dado distinto. Para o reconstruir, precisamos localizar o preço original de emissão e todos os eventos societários relevantes desde a oferta. Grupamentos e desdobramentos, isoladamente, não explicam bonificações, subscrições, cisões, incorporações, alterações de classe, distribuições ou dividendos. O relatório não deve chamar o primeiro preço histórico de “preço original do IPO” sem fonte específica.

## Fontes prioritárias
1. Relações com Investidores do emissor: comunicados, atas, avisos e histórico de eventos.
2. B3: eventos corporativos e documentos do emissor.
3. CVM: documentos periódicos e eventuais enviados pelo emissor.
4. Outras fontes, apenas como pistas para localizar a evidência primária.

Referências de método:
- B3 — [Precificação adequada das ações](https://www.b3.com.br/pt_br/produtos-e-servicos/solucoes-para-emissores/aumento-de-liquidez/precificacao-adequada-das-acoes/).
- B3 — [Eventos corporativos](https://www.b3.com.br/pt_br/noticias/eventos-corporativos.htm).
- CVM — [Sistema Empresas.NET](https://www.gov.br/cvm/pt-br/assuntos/regulados/consultas-por-participante/companhias/envio-de-informacoes-enet).

## Integração com a rotina STOCKS
Ao receber um ticker para análise, a rotina do projeto deve chamar este verificador antes de comparar preços históricos, calcular retorno de longo prazo ou construir gráficos ajustados. A conversa não dispara, por si só, um workflow do GitHub; a automação executável disponibilizada nesta versão pode ser acionada pela interface GitHub Actions (workflow_dispatch) ou localmente.