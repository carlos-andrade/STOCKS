# AÇÕES — Análise de ações da B3

Esta pasta é o diretório obrigatório de todas as análises individuais de ações brasileiras.

## Regra de criação

Quando uma ação/ticker for identificado como objeto de análise em qualquer conversa relacionada ao projeto STOCKS:
1. Confirmar o ticker e a classe do ativo na B3 (não inferir apenas pelo nome).
2. Verificar se `AÇÕES/<TICKER>/` já existe.
3. Se não existir, criar a pasta a partir de `_MODELO_ACAO/`.
4. Registar o ativo em `../registry/acoes.json` e atualizar o índice abaixo.
5. Guardar cada análise, fonte, cálculo, decisão e revisão dentro da pasta do ticker.
6. Não sobrescrever análises históricas: criar novo registo datado e manter trilha de auditoria.

**Limite operacional:** esta regra é a convenção permanente do projeto. Uma conversa não consegue, por si só, observar automaticamente todas as outras conversas; para criação global sem intervenção humana, será necessária uma integração explícita que encaminhe os tickers mencionados para o repositório.

## Índice de ações

| Ticker | Pasta | Estado |
|---|---|---|
| _MODELO_ACAO | [_MODELO_ACAO/](_MODELO_ACAO/README.md) | Modelo — não é ativo |
