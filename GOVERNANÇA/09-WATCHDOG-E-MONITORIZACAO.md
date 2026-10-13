# 09 — WATCHDOG e monitorização transversal

**Fonte normativa:** [GOVERNANCA/WATCHDOG](https://github.com/carlos-andrade/GOVERNANCA/tree/main/WATCHDOG)

O README da fonte-mãe identifica o WATCHDOG como MVP e assinala pendências na adoção transversal, supervisão independente e teste operacional de alertas/SLA. Esses estados têm de ser reconfirmados na fonte; não devem ser descritos como controlos ativos no STOCKS.

## Aplicação ao STOCKS

Inventariar ingestão, atualizações de dados, processamento analítico, relatórios e publicação. Para cada fluxo, declarar owner, importância, evidência esperada, frequência, limites de atualidade e estado de aprovação, regras de estado, escalonamento, prova de recuperação e dependências.

## Regras

- `UNKNOWN` nunca significa sucesso.
- Limites provisórios devem permanecer identificados como provisórios.
- Sem heartbeat independente, o monitor pode não detetar a própria falha.
- Alertas são operacionais apenas depois de canais, destinatários, ACK e SLA configurados e testados.
- Remediação automática fica desativada por defeito; exige escopo limitado, aprovação, rollback, logs e testes.
- Resultados devem ficar versionados e sem segredos.
- Não afirmar que STOCKS está monitorizado pelo WATCHDOG até haver integração testada e aceite neste repositório.

## Próximo passo

Inventariar os fluxos concretos do STOCKS, associar controlos e testes, implementar o adaptador e realizar aceitação específica antes de o marcar ativo.
