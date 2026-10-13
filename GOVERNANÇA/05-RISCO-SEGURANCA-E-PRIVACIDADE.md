# 05 — Risco, segurança e privacidade

**Referências:** [Gestão de risco](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/06-seguranca-e-privacidade/gestao-de-risco.md) · [Política de segurança](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/06-seguranca-e-privacidade/politica-de-seguranca.md) · [Privacidade](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/06-seguranca-e-privacidade/privacidade-e-dados-pessoais.md)

## Níveis de risco

Adotar os níveis da GOVERNANCA: **A — Essencial**, **B — Normal**, **C — Elevado**, **D — Crítico**. A classificação é específica por fluxo e pode aumentar. Informação insuficiente não significa baixo risco. A classificação interna não substitui obrigações legais ou regulatórias.

## Riscos típicos e controlos

| Risco | Controlos esperados |
|---|---|
| Dados financeiros errados/desatualizados ou unidade incorreta | Linhagem, timestamps, unidade/moeda e confronto com fonte primária. |
| Backtest enviesado ou irreprodutível | Registo dos dados, custos, universo, look-ahead/survivorship bias, parâmetros e versão do código. |
| Erro de fórmula/transformação | Testes unitários, reconciliação independente e casos-limite. |
| Credenciais expostas | Segredos fora do Git, permissões mínimas e rotação após exposição. |
| Publicação concorrente ou perda de atualização | Serialização, retry limitado, idempotência e verificação do commit final. |
| Automatização sem supervisão | Limites, logs, dry-run, kill switch, owner e rollback. |
| Fonte secundária não confirmada | Fonte primária e divergência documentada. |
| Falha de fornecedor/API | Timeout, limites, fallback explícito e estado `UNKNOWN`. |

## Segurança mínima

- Princípio do menor privilégio para tokens e workflows.
- Não incluir secrets em Markdown, issues públicas, datasets, logs ou commits.
- Rever permissões e dependências externas antes de automatizar ações.
- Separar teste e produção quando aplicável.
- Definir retenção e eliminação de dados conforme finalidade e obrigações.
- Documentar incidentes sem divulgar informação sensível.

Falha de segurança, integridade, autorização ou risco material não tratado bloqueia o fluxo afetado. Controlo compensatório exige owner, evidência, validade e aprovação apropriada.
