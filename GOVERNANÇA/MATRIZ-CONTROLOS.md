# Matriz de controlos — STOCKS

**Estado:** baseline proposto; aplicação a cada fluxo requer evidência.

| ID | Domínio | Controlo | Evidência mínima | Estado inicial |
|---|---|---|---|---|
| GOV-01 | Autoridade | Fonte normativa central identificada | Link e versão/data da norma-mãe | DOCUMENTADO |
| GOV-02 | Ownership | Owner e aprovador por fluxo | Registo RACI | PENDENTE POR FLUXO |
| GOV-03 | Risco | Classificação proporcional | Avaliação A–D e justificação | PENDENTE POR FLUXO |
| GOV-04 | Dados | Fonte, período, unidade e timestamp | Manifesto/tabela de linhagem | MODELO DOCUMENTADO; ADOÇÃO PENDENTE |
| GOV-05 | Qualidade | Testes de esquema, completude, consistência e atualidade | Relatório/artefacto de teste | PENDENTE POR FLUXO |
| GOV-06 | Decisões | Decisão material rastreada | ADR, issue ou PR | PROCEDIMENTO DOCUMENTADO |
| GOV-07 | Alterações | Diff, revisão, teste e rollback proporcionais | Commit, revisão, execução e plano | PENDENTE POR ALTERAÇÃO |
| GOV-08 | Segurança | Secrets fora do Git; privilégio mínimo | Revisão de configuração/permissões | PENDENTE DE AUDITORIA |
| GOV-09 | Privacidade | Finalidade, acesso e retenção adequados | Registo e revisão aplicável | PENDENTE POR DADO |
| GOV-10 | Release | Critérios prévios e autorização | Checklist, aprovação e evidências | PROCEDIMENTO DOCUMENTADO |
| GOV-11 | Operações | Runbook, responsável e escalonamento | Runbook e teste operacional | PENDENTE POR FLUXO |
| GOV-12 | Recuperação | Backup/restauração testados | Resultado de recuperação | PENDENTE |
| GOV-13 | Monitorização | Estados distinguem sucesso, falha e desconhecido | Configuração e resultados de teste | WATCHDOG NÃO ADOTADO LOCALMENTE |
| GOV-14 | Alertas | Canal, ACK e SLA testados | Prova de entrega e confirmação | PENDENTE |
| GOV-15 | Histórico | Snapshots materiais e decisões preservados | Commits/ficheiros datados | ADOÇÃO POR FLUXO |
| GOV-16 | IA | Inputs, limites e revisão humana definidos | Especificação, testes e aprovação | PENDENTE POR USO |
| GOV-17 | Encerramento | Aceitação, pendências e transferência | Gate G6 e lista de pendências | PENDENTE POR ENTREGA |

## Regras para alteração de estado

- `DOCUMENTADO` significa que a regra está escrita, não que o controlo está ativo.
- `IMPLEMENTADO` exige evidência de implementação.
- `TESTADO` exige teste efetivo e resultado preservado.
- `APROVADO` exige decisor autorizado e critérios cumpridos.
- `UNKNOWN` aplica-se quando a evidência é insuficiente.
- Toda a mudança deve incluir URL, commit ou artefacto e data no registo de adoção.
