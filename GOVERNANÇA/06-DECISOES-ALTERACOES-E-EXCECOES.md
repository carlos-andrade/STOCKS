# 06 — Decisões, alterações e exceções

**Referências:** [Política de decisões](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/politica-de-decisoes.md) · [Política de exceções](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/01-governanca/politica-de-excecoes.md) · [Controlo de versão e revisão](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/04-arquitetura-e-engenharia/controle-de-versao-e-revisao.md)

## Decisões a registar

Registar decisões que alterem metodologia, fontes oficiais, arquitetura, schemas, significado de indicadores, critérios de validação, escopo, acesso, automações, segurança, custos materiais ou risco residual.

## Formato ADR

Cada decisão contém ID, data, estado (`PROPOSTO`, `APROVADO`, `REJEITADO`, `SUBSTITUÍDO`), contexto, opções, pressupostos, decisão, justificação, decisor, impacto, riscos, trade-offs, ligações para requisitos/testes/evidências e condições de revisão. Guardar em `REGISTOS/decisoes/`. Decisões substituídas apontam para a sucessora; não são apagadas.

## Controlo de mudanças

1. Declarar objetivo e âmbito.
2. Identificar dados, consumidores e dependências.
3. Avaliar risco e rollback.
4. Definir testes antes da execução.
5. Rever o diff/artefacto.
6. Publicar com commit rastreável.
7. Verificar o estado após publicação.
8. Atualizar documentação, registos e roadmap.

## Exceções

Registar regra afetada, motivo, risco, impacto, controlos compensatórios, aprovador, owner, validade, plano de resolução e condição de revogação. Exceção vencida ou sem aprovação não é válida. Nenhuma exceção pode autorizar incumprimento legal ou contratual.

Preservar o histórico. Correções retroativas a evidências devem registar o motivo e a autoria.
