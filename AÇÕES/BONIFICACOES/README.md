# BONIFICAÇÕES — histórico e verificação

**ID:** STOCKS-EVENTOS-BONIFICACOES-001 · **Versão:** 1.0.0

## Regras
- Registar a percentagem anunciada e o fator total de ações após/antes em campos distintos na documentação.
- No registo canónico, `post_event_shares_per_pre_event_share` representa o fator total: 33,3333% de bonificação corresponde a aproximadamente `1.33333333333`, não a `0.33333333333`.
- Só marcar como verificado com evidência institucional específica, datas e proporção rastreáveis.
- A ausência de evento registado não prova inexistência de bonificação.

## Arquivos
- `registros.json`: registo de bonificações verificadas.
- `../VERIFICADOR_EVENTOS_SOCIETARIOS/README.md`: execução e estados do verificador.

## Fonte consultada
- [B3 — Eventos corporativos de PETR](https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/9512/PETR/corporate-actions?language=pt-BR).
