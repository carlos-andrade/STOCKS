# 08 — Operação, incidentes e continuidade

**Referências:** [Operações e observabilidade](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/07-operacoes-e-resiliencia/operacoes-e-observabilidade.md) · [Continuidade, backup e recuperação](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/07-operacoes-e-resiliencia/continuidade-backup-recuperacao.md)

## Operação

Para cada fluxo material, identificar owner, frequência, fonte de estado, limites de atualidade, dependências, alertas, logs, recuperação e canal de escalonamento.

## Registo de incidente

Registar ID, hora de deteção, intervalo afetado, sistema/dataset/processo, impacto, severidade e critério usado, evidências preservadas, mitigação, responsável, causa-raiz quando conhecida, ação corretiva/preventiva e teste de recuperação. Não inventar causa-raiz antes da investigação. Distinguir mitigação temporária de correção definitiva.

## Continuidade

Definir backup, retenção, RPO/RTO quando aplicável, dependências e recuperação. Backup só é considerado verificado após evidência de restauração/teste apropriado. Documentar um runbook não demonstra capacidade operacional real.

## Pós-incidente

Para incidente material, registar cronologia, fatores contribuintes, causa confirmada ou desconhecida, ações com owner/prazo e forma de verificar não recorrência.
