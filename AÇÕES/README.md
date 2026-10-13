# AÇÕES — Análise de ações da B3

Esta pasta é o diretório obrigatório das análises individuais e dos mecanismos comuns de validação de ações.

## Regra de criação e análise por ticker

Quando uma ação/ticker for identificado como objeto de análise no projeto STOCKS:
1. Confirmar o ticker e a classe do ativo em fonte oficial.
2. Verificar se `AÇÕES/<TICKER>/` existe; criar a pasta a partir de `_MODELO_ACAO/` se necessário.
3. Copiar o conjunto de ficheiros definido em `_MODELO_ACAO/README.md` para a pasta do ticker, removendo ou preenchendo todos os marcadores de modelo.
4. Executar o verificador de eventos societários (grupamentos, desdobramentos e bonificações) antes de calcular retornos de longo prazo ou comparar preços históricos.
5. Consultar os registos locais e as fontes oficiais do emissor, B3 e CVM.
6. Registar fontes, URLs, datas, proporções, classe de ação, validação e limitações.
7. Guardar análises e snapshots datados na pasta do ticker sem apagar histórico anterior.
8. Atualizar `registry/acoes.json` e este índice quando o ticker for efetivamente cadastrado.

**Limite operacional:** esta regra define a rotina de trabalho do projeto, mas uma conversa não consegue observar automaticamente todas as outras conversas. A verificação pode ser executada localmente ou pelo workflow GitHub Actions. Para disparo direto a partir de qualquer conversa, é necessária uma integração externa explícita.

## Estrutura transversal

- [`GRUPAMENTOS/`](GRUPAMENTOS/README.md) — registo de grupamentos verificados.
- [`DESDOBRAMENTOS/`](DESDOBRAMENTOS/README.md) — registo de desdobramentos verificados.
- [`BONIFICACOES/`](BONIFICACOES/README.md) — registo de bonificações verificadas.
- [`PETR4/`](PETR4/README.md) — dossiê de eventos históricos e investigação do preço original de emissão de PETR4.
- [`VERIFICADOR_EVENTOS_SOCIETARIOS/`](VERIFICADOR_EVENTOS_SOCIETARIOS/README.md) — CLI, esquema, testes e workflow de verificação.
- [`FONTES/`](FONTES/README.md) — catálogo de fontes do projeto.
- [`_MODELO_ACAO/`](%5FMODELO_ACAO/README.md) — modelo de dossiê por ação.
- [`_MODELO_ACAO/TESTE_LAYOUT.md`](%5FMODELO_ACAO/TESTE_LAYOUT.md) — checklist de aceitação para testar o layout noutros tickers.

## Índice de ações

| Ticker | Pasta | Estado |
|---|---|---|
| _MODELO_ACAO | [_MODELO_ACAO/](_MODELO_ACAO/README.md) | Modelo — não é ativo |
| PETR4 | [PETR4/](PETR4/README.md) | Dossiê histórico parcial; eventos/datas e preço de 1957 com pendências documentadas |
