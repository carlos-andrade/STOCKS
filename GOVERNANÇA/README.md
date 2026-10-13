# GOVERNANÇA — STOCKS

**Estado:** Estrutura inicial publicada; adoção operacional em implementação.  
**Fonte normativa:** [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA)

## Propósito

Esta pasta implementa, no contexto do STOCKS, uma camada local alinhada ao repositório-mestre GOVERNANCA. A fonte normativa permanece centralizada no repositório mestre; este diretório documenta a aplicação ao domínio de ações e os respetivos registos, controlos e evidências.

A existência destes documentos não certifica conformidade integral nem prova que todos os controlos técnicos estejam ativos.

## Princípios obrigatórios

1. **Evidência antes de alegação:** não declarar execução, teste, validação, publicação, cotação atual ou controlo ativo sem prova verificável.
2. **Fonte rastreável:** cada análise relevante identifica origem, URL, data de acesso, período, moeda/unidade e limitações.
3. **Primazia institucional:** priorizar B3, CVM, demonstrações auditadas, fatos relevantes e RI do emissor para factos corporativos.
4. **Separação de informação:** distinguir dados oficiais, derivados, estimativas, hipóteses e opinião.
5. **Controlo proporcional ao risco:** reforçar revisão e autorização conforme impacto financeiro, operacional, legal ou reputacional.
6. **Humano no circuito:** decisões materiais e exceções de alto risco exigem aprovação explícita e registada.
7. **Reversibilidade:** mudanças importantes têm histórico, responsável, critérios de aceitação e plano de recuperação adequado.
8. **Segurança e privacidade desde a conceção:** não publicar segredos, credenciais ou dados pessoais desnecessários.
9. **Sem sucesso presumido:** ausência de dados, execução ou evidência é `UNKNOWN`, não `PASS`.
10. **Preservar histórico:** não sobrescrever snapshots analíticos datados quando isso eliminar rastreabilidade.

## Hierarquia documental

1. Lei e obrigações regulatórias aplicáveis.
2. Contratos e obrigações vinculativas.
3. Políticas formalmente aprovadas na GOVERNANCA.
4. Normas e procedimentos da GOVERNANCA.
5. Esta adaptação operacional STOCKS.
6. Recomendações, notas exploratórias e exemplos.

Em caso de conflito, prevalece a fonte de maior autoridade e o conflito deve ser registado e escalado. Esta pasta não substitui aconselhamento jurídico ou aprovação formal dos proprietários.

## Estrutura documental

- [01 — Constituição e âmbito](01-CONSTITUICAO.md)
- [02 — Papéis e responsabilidades](02-PAPEIS-E-RESPONSABILIDADES.md)
- [03 — Ciclo de vida e gates](03-CICLO-DE-VIDA-E-GATES.md)
- [04 — Política de dados e evidências](04-DADOS-E-EVIDENCIAS.md)
- [05 — Risco, segurança e privacidade](05-RISCO-SEGURANCA-E-PRIVACIDADE.md)
- [06 — Decisões, alterações e exceções](06-DECISOES-ALTERACOES-E-EXCECOES.md)
- [07 — Qualidade, validação e release](07-QUALIDADE-VALIDACAO-E-RELEASE.md)
- [08 — Operação, incidentes e continuidade](08-OPERACAO-INCIDENTES-E-CONTINUIDADE.md)
- [09 — WATCHDOG e monitorização](09-WATCHDOG-E-MONITORIZACAO.md)
- [10 — Fontes normativas](10-FONTES-NORMATIVAS.md)
- [Matriz de controlos](MATRIZ-CONTROLOS.md)
- [Registo de adoção](REGISTO-ADOCAO.md)
- [Registos e modelos](REGISTOS/README.md)

## Forma mínima de adoção

Cada fluxo material deve registar owner, risco, dados e fontes, critérios de aceitação, controlos aplicáveis, evidências, estado, pendências e data de revisão. Um controlo só pode ser marcado como implementado quando houver artefacto e teste apropriados.

## Estados controlados

`PROPOSTO`, `EM_IMPLEMENTACAO`, `EM_REVISAO`, `APROVADO`, `BLOQUEADO`, `UNKNOWN`, `CONCLUIDO`, `DEPRECADO`.

## Relação com AÇÕES

Cada dossiê `AÇÕES/<TICKER>/` deve cumprir o modelo em `AÇÕES/_MODELO_ACAO/`, incluindo fontes e linhagem, qualidade dos dados, riscos, catalisadores, pressupostos, data da análise e histórico datado. Isto não garante atualidade das cotações.

## Estado inicial e limitações

Esta é a primeira camada documental local. A estrutura, as regras e os controlos propostos estão documentados; ainda é necessário verificar a adoção por cada fluxo, testar automações e ligar evidências reais. Não está declarada certificação nem adoção integral de todos os mecanismos da GOVERNANCA.

**Última revisão documental:** 2026-10-13.
