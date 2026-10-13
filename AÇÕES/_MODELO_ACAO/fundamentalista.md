# Análise fundamentalista — <TICKER>

**ID:** STOCKS-AÇÕES-FUND-001  
**Versão do modelo:** 1.0.0  
**Estado:** Modelo reutilizável — sujeito a revisão  
**Aplicação:** Ações de qualquer setor e mercado, com módulos setoriais opcionais  
**Data de referência:** AAAA-MM-DD  
**Normas:** [Governança STOCKS](../../GOVERNAN%C3%87A/README.md) · [Política de dados e evidências](../../GOVERNAN%C3%87A/04-DADOS-E-EVIDENCIAS.md)

> **Objetivo:** avaliar negócio, qualidade dos resultados, posição financeira, geração de caixa, remuneração ao acionista, valor estimado e riscos. A organização é inspirada nas categorias normalmente disponibilizadas por portais oficiais de Relações com Investidores — resultados, demonstrações financeiras, indicadores operacionais, proventos, estrutura acionária, estratégia, governança e relatórios — sem copiar conteúdo ou identidade visual de qualquer emissor.
>
> **Regra de preenchimento:** substituir campos entre sinais angulares. Quando um dado não estiver disponível, registar “ND — não disponível” e explicar a razão. Não preencher por inferência silenciosa.

---

## 1. Identificação e perímetro

- **Ticker / classe:** <TICKER / ON / PN / unit / outra>
- **Empresa / razão social:** <NOME>
- **CNPJ ou identificador legal:** <IDENTIFICADOR>
- **ISIN:** <ISIN>
- **Bolsa / mercado:** <MERCADO>
- **Setor / indústria / subsetor:** <CLASSIFICAÇÃO>
- **País e geografias principais:** <PAÍSES>
- **Moeda funcional / apresentação:** <MOEDA>
- **Unidade e escala:** <unidades / milhares / milhões>
- **Perímetro contabilístico:** <consolidado / individual / ambos>
- **Padrão contabilístico:** <IFRS / CPC / US GAAP / outro>
- **Exercício fiscal:** <início e fim>
- **Website de Relações com Investidores:** <URL>
- **Data de corte dos dados:** <AAAA-MM-DD>
- **Analista / revisor:** <RESPONSÁVEL>
- **Estado:** <NÃO INICIADA / EM ANÁLISE / VALIDADA / DESATUALIZADA>

### 1.1 Pergunta e horizonte
- **Objetivo da análise:** <qual decisão ou hipótese será informada>
- **Horizonte de investimento:** <prazo e justificação>
- **Referência de comparação:** <índice, concorrentes ou custo de capital>
- **Limitações conhecidas:** <dados, período, cobertura ou metodologia>

## 2. Resumo executivo

- **Modelo de negócio:** <como cria e captura valor>
- **Motores de receita e lucro:** <principais fatores>
- **Vantagens competitivas e evidências:** <lista>
- **Fragilidades principais:** <lista>
- **Qualidade financeira e geração de caixa:** <conclusão fundamentada>
- **Alocação de capital e remuneração:** <conclusão fundamentada>
- **Valuation preliminar:** <faixa, método, moeda e data>
- **Tese-base:** <síntese>
- **Condição que invalida a tese:** <condição observável>
- **Confiança na análise:** <ALTA / MÉDIA / BAIXA e justificação>

## 3. Fontes, integridade e qualidade dos dados

### 3.1 Hierarquia de fontes
Priorizar, conforme o dado procurado:
1. Demonstrações financeiras, releases, formulários e relatórios oficiais do emissor.
2. Regulador e bolsa do mercado relevante (por exemplo, CVM e B3 no Brasil).
3. Comunicados, fatos relevantes, políticas, atas e documentos oficiais de governança.
4. Fontes secundárias identificadas como tal, para contexto ou comparação.

### 3.2 Proveniência dos dados

| Campo / indicador | Valor | Período de referência | Publicação | Moeda / unidade | Fonte e URL específica | Tipo | Validação |
|---|---|---|---|---|---|---|---|
| <CAMPO> | <VALOR> | <PERÍODO> | <DATA> | <UNIDADE> | <URL> | Reportado / calculado / estimado | PASS / WARN / FAIL / UNKNOWN |

- **Documentos primários consultados:** <lista e links>
- **Último balanço disponível:** <período e data de publicação>
- **Estado da informação:** <auditada / revisada / preliminar>
- **Restatements ou reclassificações:** <descrição ou ND>
- **Divergências entre fontes:** <divergência, resolução e justificação>
- **Dados em falta e impacto:** <lista>
- **Data/hora de captura e fuso:** <timestamp e fuso>

Não misturar períodos trimestrais, acumulados e anuais; bases individuais e consolidadas; moedas, unidades ou escalas; números reportados e ajustados; ou valores nominais e corrigidos sem identificação explícita.

## 4. Negócio, setor e vantagem competitiva

- **Produtos e serviços:** <lista>
- **Segmentos de negócio e contribuição para receita/lucro:** <segmentos>
- **Clientes, fornecedores e concentração:** <dados divulgados>
- **Mercados e exposição geográfica:** <dados>
- **Ciclo económico e fatores de procura:** <fatores>
- **Sensibilidade a juros, inflação, câmbio e commodities:** <exposição>
- **Concorrentes comparáveis e critério de seleção:** <lista e justificação>
- **Barreiras à entrada, poder de preço e custos de mudança:** <evidências>
- **Regulação, licenças e concessões relevantes:** <regras, prazos e riscos>
- **Dependências críticas:** <ativos, tecnologia, clientes ou fornecedores>

## 5. Desempenho financeiro histórico

Preencher, preferencialmente, pelo menos cinco exercícios anuais e os últimos oito trimestres, quando disponíveis. Identificar período, moeda, unidade, perímetro e fonte.

| Indicador | Período atual | Período anterior | Variação | Unidade | Fonte / observações |
|---|---:|---:|---:|---|---|
| Receita líquida | | | | | |
| Lucro bruto | | | | | |
| EBITDA reportado | | | | | |
| EBITDA ajustado e reconciliação | | | | | |
| EBIT / resultado operacional | | | | | |
| Resultado financeiro | | | | | |
| Lucro líquido atribuível aos acionistas | | | | | |
| Lucro por ação (LPA/EPS) | | | | | |
| Margem bruta | | | | % | |
| Margem EBITDA | | | | % | |
| Margem EBIT | | | | % | |
| Margem líquida | | | | % | |

### 5.1 Tendências e explicações
- **Crescimento de receita:** <CAGR, períodos, base e fatores>
- **Evolução das margens:** <tendência e fatores>
- **Itens não recorrentes:** <valor, natureza e tratamento>
- **Efeitos cambiais, inflação e preços de referência:** <impacto>
- **Aquisições, alienações e mudanças de perímetro:** <impacto>
- **Qualidade e recorrência dos resultados:** <avaliação fundamentada>

## 6. Balanço e solvência

| Indicador | Período atual | Período anterior | Unidade | Fonte / observações |
|---|---:|---:|---|---|
| Caixa e equivalentes | | | | |
| Dívida bruta | | | | |
| Dívida líquida, com definição | | | | |
| Dívida líquida / EBITDA | | | x | |
| Dívida / patrimônio líquido | | | x ou % | |
| Ativo total | | | | |
| Património líquido | | | | |
| Liquidez corrente, quando aplicável | | | x | |
| Obrigações de curto prazo | | | | |
| Provisões e contingências relevantes | | | | |

- **Vencimentos da dívida:** <curto / médio / longo prazo>
- **Moedas, taxas fixas/variáveis e garantias:** <detalhes>
- **Covenants e folga de cumprimento:** <detalhes>
- **Passivos fiscais, judiciais, ambientais ou de pensões:** <detalhes>
- **Risco de refinanciamento:** <avaliação e evidência>

## 7. Geração de caixa e alocação de capital

| Indicador | Período atual | Período anterior | Unidade | Fonte / observações |
|---|---:|---:|---|---|
| Fluxo de caixa operacional (FCO/CFO) | | | | |
| Investimento em ativos (CAPEX) | | | | |
| Fluxo de caixa livre, com definição | | | | |
| Aquisições / alienações | | | | |
| Juros pagos | | | | |
| Dividendos e JCP pagos | | | | |
| Recompras / emissões de ações | | | | |

- **Definição de fluxo de caixa livre:** <FCO menos CAPEX ou outra fórmula>
- **Conversão de lucro em caixa:** <método, resultado e período>
- **Capital de giro:** <tendência e efeito>
- **CAPEX de manutenção vs. expansão:** <dados divulgados ou ND>
- **Retorno de investimentos e projetos:** <evidência>
- **Disciplina de alocação de capital:** <investimento, dívida, aquisições, proventos e recompras>
- **Necessidades futuras de capital:** <estimativa e pressupostos>

## 8. Rentabilidade e eficiência

| Indicador | Valor | Período | Fórmula / definição | Fonte / inputs |
|---|---:|---|---|---|
| ROE | | | Lucro líquido / patrimônio líquido médio, ou definição identificada | |
| ROA | | | Lucro líquido / ativo médio, ou definição identificada | |
| ROIC | | | NOPAT / capital investido médio, com componentes identificados | |
| Giro de ativos | | | Receita / ativo médio | |
| Margem operacional | | | EBIT / receita líquida | |
| Custo de capital (WACC ou equivalente) | | | Premissas documentadas | |

Usar médias de saldos quando a fórmula assim o exigir. Não comparar indicadores com definições diferentes sem normalização e nota metodológica.

## 9. Dividendos, JCP e remuneração ao acionista

- **Política oficial de remuneração:** <URL, data e síntese>
- **Histórico por evento:** <manter tabela histórica própria>
- **Valor bruto por ação e tipo de provento:** <dados>
- **Data de anúncio, data-com/data-base e pagamento:** <dados>
- **Dividend yield histórico:** <valor, janela, preço de referência e fórmula>
- **Dividend yield projetado:** <cenário, pressupostos e incerteza>
- **Payout sobre lucro:** <fórmula, período e resultado>
- **Payout sobre fluxo de caixa livre:** <fórmula, período e resultado>
- **Cobertura dos proventos pelo caixa:** <análise>
- **Regularidade e volatilidade dos pagamentos:** <análise>
- **Retenção de lucros, recompra e diluição:** <análise>
- **Tributação e diferenças por classe/mercado:** <regras e fonte>

Distinguir provento anunciado, aprovado, declarado, a pagar e efetivamente pago. Não tratar yield passado como promessa de rendimento futuro.

## 10. Estrutura acionária, liquidez e direitos

- **Ações emitidas por classe:** <quantidade e data>
- **Ações em tesouraria:** <quantidade>
- **Free float:** <valor, definição e data>
- **Controlador e participações relevantes divulgadas:** <dados>
- **Direitos económicos e políticos da classe analisada:** <fonte oficial>
- **Segmento de listagem e práticas de governança:** <dados>
- **Valor de mercado:** <preço × ações, data, classe e perímetro>
- **Liquidez de negociação:** <volume/valor médio, janela e fonte>
- **Eventos societários:** <desdobramento, grupamento, bonificação, subscrição, conversão ou outro>

Confirmar ticker, classe e ISIN em fonte oficial. Não assumir que todos os indicadores da empresa são específicos de uma classe de ações.

## 11. Indicadores operacionais e módulo setorial

Selecionar apenas os indicadores relevantes para o negócio. Identificar definição, unidade, periodicidade, fonte e comparabilidade.

| Indicador operacional | Valor | Período | Unidade | Definição / fonte |
|---|---:|---|---|---|
| <KPI 1> | | | | |
| <KPI 2> | | | | |
| <KPI 3> | | | | |

### Guia de módulos opcionais
- **Petróleo, gás e mineração:** produção, reservas, custo unitário, preço realizado, vida útil dos ativos, CAPEX e exposição a commodities.
- **Bancos:** margem financeira, custo do risco, inadimplência, cobertura, capital regulatório, ROE e liquidez.
- **Seguradoras:** prémios, sinistralidade, combined ratio, solvência e resultado financeiro.
- **Imobiliário / REIT / FIIs:** ocupação, renda comparável, NOI, FFO/AFFO, LTV, maturidade dos contratos e vacância.
- **Utilities / concessões:** volume distribuído, perdas, disponibilidade, tarifas, base regulatória, CAPEX e qualidade do serviço.
- **Retalho / consumo:** vendas comparáveis, volume, ticket médio, margem, inventário, giro e vendas por área.
- **Tecnologia / SaaS:** receita recorrente, crescimento orgânico, retenção, churn, margem bruta e custo de aquisição, quando divulgados.
- **Indústria / transporte:** volume, utilização da capacidade, custo unitário, produtividade, backlog e segurança operacional.

Não preencher métricas que não se aplicam à empresa nem comparar KPIs com definições incompatíveis.

## 12. Estratégia, projeções e catalisadores

- **Plano estratégico divulgado:** <documento, data e URL>
- **Metas oficiais e horizonte:** <metas, prazos e pressupostos da empresa>
- **Investimentos e projetos relevantes:** <valor, prazo, retorno esperado e riscos>
- **Catalisadores positivos:** <evento, horizonte e mecanismo>
- **Catalisadores negativos:** <evento, horizonte e mecanismo>
- **Consenso de analistas, se utilizado:** <fonte, data e cobertura; não é dado oficial do emissor>
- **Separação entre guidance, consenso e estimativa própria:** <explicitar>

## 13. Valuation

Registar preço e valor estimado na mesma data de referência, sempre que possível. Identificar se o preço é de fecho, atrasado ou intradiário e a respetiva fonte.

### 13.1 Dados-base
- **Preço por ação:** <valor, moeda, data e fonte>
- **Ações diluídas relevantes:** <quantidade e data>
- **Capitalização bolsista:** <valor e método>
- **Dívida líquida:** <valor, data e definição>
- **Valor da firma (EV):** <valor e fórmula>
- **LPA / EPS:** <valor, período e base>
- **Valor patrimonial por ação:** <valor, data e base>

### 13.2 Múltiplos

| Métrica | Valor | Período / base | Comparáveis | Observações |
|---|---:|---|---|---|
| P/L | | | | |
| P/VP | | | | |
| EV/EBITDA | | | | |
| EV/EBIT | | | | |
| FCF yield | | | | |
| Dividend yield | | | | |
| Métrica setorial | | | | |

Indicar quando um múltiplo não é significativo, por exemplo, devido a lucro negativo ou denominador não representativo.

### 13.3 Método e pressupostos
- **Método(s):** <DCF / dividendos / múltiplos / NAV / residual income / outro>
- **Justificação da escolha:** <adequação ao setor e negócio>
- **Pressupostos principais:** <crescimento, margens, CAPEX, capital de giro, impostos, WACC, crescimento terminal ou outros>
- **Reconciliação entre EV e capital próprio:** <cálculo>
- **Valor estimado por ação:** <faixa, moeda e data>
- **Sensibilidade:** <variáveis e impacto>
- **Comparáveis e diferenças estruturais:** <justificação>
- **Limitações do método:** <lista>

## 14. Cenários e margem de segurança

| Variável | Pessimista | Base | Otimista |
|---|---:|---:|---:|
| Crescimento / volume | | | |
| Margem / preço realizado | | | |
| CAPEX / capital de giro | | | |
| Custo de capital / taxa de desconto | | | |
| Valor estimado por ação | | | |
| Probabilidade atribuída, se utilizada | | | |

- **Valor intrínseco de referência:** <valor, método e data>
- **Preço de mercado de referência:** <valor e data>
- **Margem de segurança:** <fórmula, resultado e limitações>
- **Principais sensibilidades:** <variáveis>
- **Eventos que invalidam os cenários:** <condições>

Probabilidades só devem ser usadas quando houver método e justificação; não são factos observados.

## 15. Governança, riscos e sustentabilidade

- **Conselho e administração:** <fonte e data>
- **Controlador, partes relacionadas e conflitos de interesse:** <evidências>
- **Remuneração e incentivos da administração:** <política e métricas>
- **Auditor independente e opinião:** <relatório, data e ressalvas>
- **Contingências e investigações divulgadas:** <fonte, estado e impacto>
- **Riscos regulatórios, políticos e jurídicos:** <exposição>
- **Riscos financeiros e operacionais:** <exposição>
- **Riscos climáticos, ambientais e sociais materiais:** <evidência e impacto>
- **Incidentes, controvérsias e resposta da empresa:** <factos verificados e fontes>
- **Mitigações e indicadores de acompanhamento:** <medidas e métricas>

Distinguir risco potencial, evento divulgado, investigação em curso e conclusão formal. Não converter alegações em factos confirmados sem evidência adequada.

## 16. Tese e conclusão

- **Tese otimista:** <condições, evidências e catalisadores>
- **Tese-base:** <condições, evidências e catalisadores>
- **Tese pessimista:** <condições, evidências e catalisadores>
- **Vantagens comprovadas:** <lista>
- **Fragilidades materiais:** <lista>
- **Condições de invalidação:** <sinais observáveis>
- **Indicadores a acompanhar nos próximos resultados:** <lista>
- **Valuation e intervalo de valor:** <resultado, data e método>
- **Margem de segurança:** <resultado ou ND>
- **Conclusão analítica:** <síntese equilibrada>
- **Confiança e limitações:** <nível e justificação>
- **Estado da tese:** <EM OBSERVAÇÃO / REVER / INVALIDADA / OUTRO>

A conclusão não deve depender de um múltiplo isolado ou de um dividend yield. Se houver recomendação de investimento, explicitar horizonte, pressupostos e riscos, sem prometer retorno.

## 17. Atualização e histórico

- **Frequência de atualização:** <trimestral / semestral / anual / por evento>
- **Próxima revisão:** <data ou condição>
- **Gatilhos extraordinários:** <resultado, fato relevante, alteração de guidance, operação societária ou outro>
- **Versão da metodologia / código de cálculo:** <versão ou ND>
- **Snapshot histórico:** guardar em historico/AAAA-MM-DD.md, sem apagar versões anteriores.
- **Alterações desde a revisão anterior:** <dados, método, tese e conclusão>
- **Revisor e data:** <responsável / data>

## 18. Checklist de validação

- [ ] Ticker, classe, ISIN e emissor confirmados em fonte oficial.
- [ ] Data de referência, moeda, unidade, escala e perímetro identificados.
- [ ] Períodos trimestrais, acumulados e anuais não foram misturados.
- [ ] Demonstrações e releases reconciliados, quando aplicável.
- [ ] Indicadores ajustados têm definição e reconciliação.
- [ ] Fórmulas, inputs e datas dos indicadores derivados foram registados.
- [ ] Proventos distinguem anúncio, aprovação, data-base e pagamento.
- [ ] Preço e denominadores do valuation são compatíveis em data e classe.
- [ ] Dados ausentes, divergências e limitações estão explícitos.
- [ ] Cenários, riscos e condições de invalidação estão documentados.
- [ ] URLs específicas e documentos de suporte constam em fontes.md.
- [ ] Revisão de qualidade concluída e evidência preservada.

**Resultado da validação:** <PASS / WARN / FAIL / UNKNOWN>  
**Evidência:** <URL, commit, relatório ou registo>  
**Pendências impeditivas:** <lista ou nenhuma>

---

## Referências-base a preencher para cada emissor

- **Relações com Investidores:** <URL>
- **Central de resultados / demonstrações financeiras:** <URL>
- **Comunicados / fatos relevantes / avisos aos acionistas:** <URL>
- **Relatórios anuais / formulário de referência:** <URL>
- **Dividendos e política de remuneração:** <URL>
- **Composição acionária e direitos da classe:** <URL>
- **Indicadores operacionais e setoriais:** <URL>
- **Regulador:** <URL>
- **Bolsa / dados de negociação:** <URL>

**Fonte de referência para o piloto PETR4:** Petrobras RI — https://www.investidorpetrobras.com.br/ (Central de Resultados, Comunicados, Relatórios Anuais, Indicadores, Composição Acionária e Dividendos/JCP). A disponibilidade, periodicidade e formato devem ser verificados em cada recolha; a existência de uma página não significa que os dados tenham sido importados ou validados.
