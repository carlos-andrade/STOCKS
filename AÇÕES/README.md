# AÇÕES — Análise de ações da B3

Esta pasta é o diretório obrigatório das análises individuais e dos mecanismos comuns de validação de ações.

## Regra de criação e análise por ticker

Quando uma ação/ticker for identificado como objeto de análise no projeto STOCKS:
1. Confirmar o ticker e a classe do ativo em fonte oficial.
2. Verificar se `AÇÕES/<TICKER>/` existe; criar a pasta a partir de `_MODELO_ACAO/` se necessário.
3. Executar o verificador de eventos societários (grupamentos, desdobramentos e bonificações) antes de calcular retornos de longo prazo ou comparar preços históricos.
4. Consultar os registos locais e as fontes oficiais do emissor, B3 e CVM.
5. Registar fontes, URLs, datas, proporções, classe de ação, validação e limitações.
6. Guardar análises e snapshots datados na pasta do ticker sem apagar histórico anterior.

**Limite operacional:** esta regra define a rotina de trabalho do projeto, mas uma conversa não consegue observar automaticamente todas as outras conversas. A verificação pode ser executada localmente ou pelo workflow GitHub Actions. Para disparo direto a partir de qualquer conversa, é necessária uma integração externa explícita.

## Estrutura transversal

- [`GRUPAMENTOS/`](GRUPAMENTOS/README.md) — registo de grupamentos verificados.
- [`DESDOBRAMENTOS/`](DESDOBRAMENTOS/README.md) — registo de desdobramentos verificados.
- [`BONIFICACOES/`](BONIFICACOES/README.md) — registo de bonificações verificadas.
- [`PETR4/`](PETR4/README.md) — dossiê de eventos históricos e investigação do preço original de emissão de PETR4.
- [`VERIFICADOR_EVENTOS_SOCIETARIOS/`](VERIFICADOR_EVENTOS_SOCIETARIOS/README.md) — CLI, esquema, testes e workflow de verificação.
- [`FONTES/`](FONTES/README.md) — catálogo de fontes do projeto.
- [`_MODELO_ACAO/`](%5FMODELO_ACAO/README.md) — modelo de dossiê por ação.

## Índice de ações

| Ticker | Pasta | Estado |
|---|---|---|
| _MODELO_ACAO | [_MODELO_ACAO/](_MODELO_ACAO/README.md) | Modelo — não é ativo |
