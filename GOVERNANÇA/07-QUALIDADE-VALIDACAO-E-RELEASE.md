# 07 — Qualidade, validação e release

**Referências:** [Conformidade documental](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/politica-de-conformidade-documental.md) · [Padrões de arquitetura e engenharia](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/04-arquitetura-e-engenharia/arquitetura-e-padroes.md)

## Qualidade analítica

Antes de concluir uma análise material, verificar ticker e entidade; período e base contabilística; unidades, moedas e ajustes societários; fontes, datas e limitações; reprodutibilidade dos cálculos; pressupostos e cenários; riscos, catalisadores e condições de invalidação; e coerência entre evidência, incerteza e conclusão.

## Qualidade de código e automação

- Rever o diff e o âmbito.
- Executar testes adequados, incluindo casos negativos e limites.
- Tratar entradas inválidas de forma previsível.
- Garantir reexecução segura/idempotência onde aplicável.
- Preservar logs sem segredos e identificadores rastreáveis.
- Usar permissões mínimas e versões suportadas.
- Guardar o resultado de execução.

## Critério de release

Marcar release como `APROVADO` apenas quando critérios pré-definidos são cumpridos e as evidências estão anexadas. Um commit prova gravação de código, não funcionamento. Um workflow verde prova apenas os controlos realmente executados nesse workflow. Registar explicitamente `NÃO TESTADO` ou `UNKNOWN` sempre que aplicável.
