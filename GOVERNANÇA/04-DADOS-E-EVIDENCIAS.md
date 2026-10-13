# 04 — Política de dados, fontes e evidências

**Referências:** [Governança de dados](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/05-dados-e-ia/governanca-de-dados.md) · [Qualidade e linhagem](https://github.com/carlos-andrade/GOVERNANCA/blob/main/docs/05-dados-e-ia/qualidade-e-linhagem.md) · [Fontes no modelo de ação](../A%C3%87%C3%95ES/_MODELO_ACAO/fontes.md) · [Catálogo de fontes STOCKS](../A%C3%87%C3%95ES/FONTES/README.md)

## Classes de informação

1. **Fonte oficial primária:** bolsa, regulador, divulgação oficial, demonstração auditada ou RI do emissor.
2. **Fonte operacional interna:** repositórios e workflows; úteis para processos e evidências de execução, não necessariamente para factos do emissor.
3. **Dado derivado:** calculado a partir de fontes identificadas, com transformação rastreável.
4. **Estimativa / hipótese:** dependente de pressupostos explícitos e sensibilidade quando relevante.
5. **Opinião / interpretação:** juízo analítico separado dos factos.
6. **Desconhecido:** origem, período ou validade insuficientes.

## Metadados mínimos

Registar nome e descrição; ticker/identificador e granularidade; fonte e URL específico; data de publicação/acesso; período e fuso horário; moeda e unidade; transformações e versão da metodologia; frequência e limite de atualidade; completude e limitações; responsável e localização da evidência.

## Regras para dados de mercado e financeiros

- Diferenciar último preço, cotação atrasada, fecho, ajuste e histórico.
- Identificar moeda, unidade, lote e escala (por exemplo, milhares) quando aplicável.
- Verificar desdobramentos, grupamentos, dividendos e revisões históricas antes de comparar séries.
- Não misturar períodos contabilísticos ou bases individuais/consolidadas sem sinalização.
- Registar fórmula, inputs e timestamp em dados derivados quando possível.
- Identificar se valores financeiros são auditados, preliminares ou estimados.
- Documentar divergências entre fontes e a regra usada para as resolver.

## Qualidade e evidência

Definir verificações apropriadas: schema, tipos, intervalos, duplicados, dados ausentes, reconciliação, completude, atualidade, consistência temporal e proveniência. Teste só passa se critério, resultado e evidência forem consultáveis. Preferir URL imutável, commit SHA, artefacto de workflow, log de teste ou documento oficial. Não afirmar sincronização de todos os chats sem mecanismo externo e teste específico.
