# 03 — Ciclo de vida e gates

**Referência:** [Ciclo de vida e gates da GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md)

Ciclo padrão: propor → classificar risco → planear → desenhar → executar → validar → publicar/operar → observar → melhorar → encerrar.

| Gate | Objetivo | Evidência mínima | Regra de decisão |
|---|---|---|---|
| G0 — Entrada | Clarificar problema e ownership | Objetivo, âmbito, beneficiário, owner | Sem owner/objetivo, devolver. |
| G1 — Viabilidade | Avaliar valor e risco | Alternativas, dependências, pressupostos, esforço e risco | Alto risco/desconhecido exige revisão. |
| G2 — Desenho | Tornar solução segura e testável | Arquitetura, fontes, dados, ameaças, critérios e testes | Não construir integração crítica sem contratos. |
| G3 — Construção validada | Demonstrar qualidade | Revisão, testes, artefactos e documentação | Falha ou evidência insuficiente bloqueia. |
| G4 — Prontidão | Preparar operação e recuperação | Alertas, responsáveis, backup, rollback e runbook | Não declarar pronto sem verificar controlos aplicáveis. |
| G5 — Publicação | Controlar a alteração | Commit/release, autorização, janela, métricas e rollback | Publicação não prova validação funcional. |
| G6 — Encerramento | Confirmar aceitação e transferência | Aceitação, pendências, retenção/eliminação e lições | Pendências ficam explícitas. |

Gates podem ser combinados em atividades reversíveis de baixo risco, com justificação. Não dispensam obrigações legais/contratuais, controlos críticos nem autorização necessária. Cada gate precisa de decisor autorizado, critérios definidos previamente e evidência ligada ao resultado.
