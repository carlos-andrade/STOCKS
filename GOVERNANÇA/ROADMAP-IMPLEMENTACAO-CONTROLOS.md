# Roadmap de implementação dos controlos — STOCKS

**Estado:** Planeamento inicial, sujeito a validação da árvore completa e aprovação de owners.  
**Fonte normativa:** `GOVERNANÇA/` e [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).

## Regras de execução

- Executar na ordem abaixo; não declarar conclusão apenas por criar documentação.
- Não ativar automação que escreva ou altere dados sem testes e autorização explícita.
- Não ativar remediação automática no WATCHDOG por defeito.
- Para cada marco, guardar evidência, resultado, commit/URL, responsável, pendências e data.
- Se o owner não estiver formalmente identificado, manter o marco `BLOQUEADO` ou `UNKNOWN` quanto à aprovação.

## Fases

| Fase | Entrega | Critério de saída | Estado inicial |
|---|---|---|---|
| P0 — Inventário | Inventário de ficheiros, workflows, scripts, datasets e tickers | Árvore completa inspecionada; cada caminho classificado e evidência ligada | PARCIAL — leitura de caminhos conhecidos concluída; árvore integral pendente |
| P1 — Ownership e risco | RACI e avaliação de risco por fluxo | Owner/approver definidos e risco justificado | PENDENTE |
| P2 — Integridade documental | Índice, schema e validação de links/caminhos | Teste reproduzível e resultado preservado | PENDENTE |
| P3 — Registo de ações | `registry/acoes.json` com schema e regra de unicidade | Testes de ticker, duplicados e consistência do índice aprovados | PENDENTE |
| P4 — Criação automatizada | Script/workflow para gerar dossier a partir do modelo | Dry-run, testes negativos, idempotência e revisão; sem duplicar ticker | PENDENTE |
| P5 — Dados e análises | Inventário de fontes/datasets e contratos de qualidade | Proveniência, atualidade, unidades, reconciliação e logs definidos | PENDENTE |
| P6 — Segurança e release | Revisão de permissões, secrets, branches e processo de release | Evidência de revisão e testes de proteção aplicáveis | PENDENTE |
| P7 — WATCHDOG em modo observação | Inventário monitorizado e avaliação read-only | Estados PASS/WARN/FAIL/UNKNOWN testados; limites aprovados; logs e owner definidos | NÃO INICIADO LOCALMENTE |
| P8 — Alertas e supervisão | Canal, ACK, SLA e heartbeat independente quando aplicável | Testes positivos e negativos, incluindo ausência de heartbeat | PENDENTE |
| P9 — Aceitação | Revisão do conjunto e aprovação | Critérios satisfeitos, pendências residuais aceites e evidência publicada | PENDENTE |

## Ordem de prioridade

1. Completar o inventário técnico e confirmar owners.
2. Corrigir lacunas de integridade e criar registo central validado.
3. Automatizar a criação de dossiers apenas depois de schema/testes.
4. Estabelecer contratos de qualidade para cada fonte/dataset antes de consumir dados em análises.
5. Rever segurança e release antes de ligar automações.
6. Integrar WATCHDOG read-only, primeiro com sinais/evidências de teste, depois com fontes reais.
7. Só depois testar alertas, heartbeat e SLA. A ausência de integração externa deve permanecer explícita.

## Estados padronizados

`NÃO INICIADO`, `EM CURSO`, `BLOQUEADO`, `UNKNOWN`, `EM REVISÃO`, `APROVADO`, `CONCLUÍDO`.

O estado `APROVADO` requer decisor autorizado; `CONCLUÍDO` requer critérios de saída e evidências. Percentuais só serão calculados quando houver método e evidência de conclusão por fase; não atribuir percentuais arbitrários.
