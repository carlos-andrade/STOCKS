# 01 — Constituição local de governança STOCKS

**ID:** STOCKS-GOV-001 · **Versão:** 1.0.0 · **Estado:** Proposto para revisão e aprovação operacional  
**Norma-mãe:** [CONSTITUICAO.md — GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CONSTITUICAO.md)

## Finalidade

Estabelecer limites e princípios para gerir dados, análises, ferramentas, automações e decisões documentadas no repositório STOCKS.

## Princípios locais

- Cada análise material declara pergunta, objetivo, universo, período e decisão que procura informar.
- Cada métrica tem definição, unidade, frequência, fonte e transformação documentadas.
- Dados ausentes ou inconsistentes não são substituídos silenciosamente por pressupostos.
- O conteúdo de e-mails, mensagens, notícias ou repositórios internos não é, só por isso, fonte oficial.
- Nenhum backtest ou indicador constitui prova de rentabilidade futura.
- Resultados calculados devem ser reproduzíveis a partir de inputs, versão de código e metodologia registados, quando tecnicamente possível.
- Operações destrutivas, publicações externas, alterações de produção e decisões de investimento material exigem autorização conforme o risco.
- Repositórios de projeto podem manter documentos locais, mas a norma central permanece em GOVERNANCA.
- O registo de uma fonte não significa que ela tenha sido consultada ou validada numa análise específica.

## Hierarquia e resolução de conflito

Aplicar a hierarquia descrita no [README](README.md). Dúvidas ou conflitos são registados em `REGISTOS/decisoes/` e encaminhados ao responsável autorizado. Enquanto um conflito material estiver por resolver, o fluxo afetado fica bloqueado ou explicitamente limitado.

## Regras de integridade

É proibido afirmar que houve leitura integral quando apenas um resumo foi consultado; declarar teste sem resultado verificável; tratar preço histórico, atrasado e em tempo real como equivalentes; ocultar limitações relevantes; substituir evidência histórica sem registar a correção; ou incluir credenciais, tokens e dados pessoais desnecessários no Git.

## Revisão

Rever perante alteração material na norma-mãe, incidente significativo, alteração regulatória aplicável ou periodicidade definida pelo responsável do projeto.
