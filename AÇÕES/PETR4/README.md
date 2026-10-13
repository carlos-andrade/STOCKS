# PETR4 — Dossiê de eventos societários e origem do preço

**Emissor:** Petróleo Brasileiro S.A. — Petrobras  
**Ticker analisado:** PETR4 (ação preferencial)  
**Data da pesquisa:** 2026-10-13  
**Estado da cobertura histórica:** PARCIAL — não equivale a reconstrução completa de capital nem a determinação do preço original de IPO.

## Eventos históricos identificados

| Data/posição de referência | Evento | Fator total de ações após/antes | Data efetiva/ex-date | Estado |
|---|---|---:|---|---|
| 02/07/1993; 05/07/1993 indicada por fonte secundária | Desdobramento: 79 ações novas por ação antiga | 80,0 | 05/07/1993 não confirmada em fonte primária consultada | PENDENTE — fator documentado no relatório anual |
| 25/03/1994 | Bonificação de 33,333333333% | 1,33333333333 | 28/03/1994 inferida; pendente de confirmação | PENDENTE |
| 21/06/2000 | Grupamento 100:1 | 0,01 | 23/06/2000 inferida após feriado em 22/06; pendente de confirmação | PENDENTE |
| 31/08/2005 | Desdobramento 4:1 (três ações novas por ação antiga) | 4,0 | 01/09/2005 | VERIFICADO |
| 25/04/2008 | Desdobramento de 100% (uma ação adicional por ação existente) | 2,0 | Efeito societário reportado a partir de 25/04/2008; negociação ajustada a partir de 28/04/2008 | VERIFICADO |

### Fontes e interpretação

- **1993:** o relatório anual da Petrobras descreve a AGE de 02/07/1993 e a emissão de 79 ações novas por ação existente (fator total 80). Cópia arquivada em [Biblioteca Digital AEPET — Relatório anual 1993](https://bibliotecadigital.aepet.org.br/wp-content/uploads/2024/01/Relatorio-anual-1993.pdf). O [Decreto de 02/07/1993 no Senado Federal](https://legis.senado.leg.br/norma/375645/publicacao/15655719) confirma a alteração estatutária/capital, mas não informa isoladamente a proporção. A data de negociação ajustada de 05/07/1993 ainda precisa de confirmação primária específica.
- **1994 e 2000:** a [B3 — Eventos corporativos de PETR](https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/9512/PETR/corporate-actions?language=pt-BR) indica a bonificação de 33,333333333%, o grupamento com fator 0,01 e os últimos dias para negociar com direito. A B3 usa a coluna “Negócios com até”; ela não deve ser copiada automaticamente para o campo de data ex. As datas 28/03/1994 e 23/06/2000 são inferências, não datas confirmadas pela fonte primária consultada. O dia 22/06/2000 foi feriado de Corpus Christi.
- **2005:** o [Form 20-F da Petrobras arquivado na SEC](https://www.sec.gov/Archives/edgar/data/1119639/000095012307009305/y36368a1e20vfza.htm) confirma que a AGE de 22/07/2005 aprovou a conversão de cada ação em quatro ações, com base na posição de 31/08/2005 e vigência a partir de 01/09/2005.
- **2008:** a B3 regista desdobramento de 100% (uma ação adicional por ação existente). O [documento da Petrobras arquivado na SEC](https://www.sec.gov/Archives/edgar/data/831001/000119312510139139/dfwp.htm) indica que a cotação ajustada passou a refletir o desdobramento a partir de 28/04/2008. A data societária e a data de negociação ajustada são campos diferentes.

O fator foi normalizado para o contrato de dados STOCKS: ações totais após o evento divididas pelas ações antes do evento. Para o desdobramento de 2008, o valor “100” exibido pela B3 é a percentagem de desdobramento, não um fator total 100x.
## Candidatos ainda não confirmados

- **05/07/1993 — alegado desdobramento 80:1:** não foi confirmado na tabela consultada da B3 nem foi localizada, nesta revisão, evidência primária específica. Não incorporar como evento confirmado.
- **2005 — alegado desdobramento 4:1:** não foi confirmado na tabela consultada da B3 nem foi localizada, nesta revisão, evidência primária específica. Não incorporar como evento confirmado.

Estes pontos permanecem pendentes de pesquisa em documentos históricos da companhia/CVM; a ausência na tabela atual da B3 não prova que nunca ocorreram.

## Preço original de emissão / IPO

**Estado: UNKNOWN — preço original de IPO não estabelecido.** Não confundir valor nominal legal, preço de subscrição, preço de oferta pública e primeira cotação observada.

A [Lei nº 2.004, de 3 de outubro de 1953, art. 9º](https://www2.camara.leg.br/legin/fed/lei/1950-1959/lei-2004-3-outubro-1953-366242-publicacaooriginal-1-pl.html) definiu capital inicial de Cr$ 4.000.000.000,00 dividido em 20.000.000 ações ordinárias nominativas de Cr$ 200,00 cada. Esse valor legal nominal de 1953 **não comprova o preço de uma oferta pública inicial nem o preço de negociação da PETR4**. O Formulário de Referência da companhia informa que as ações ON e PN foram listadas na Bolsa do Rio em agosto de 1956 e que o primeiro negócio ocorreu em dezembro de 1957; esse marco histórico também não fornece, por si só, o preço do primeiro negócio. Fonte de referência histórica: [documento de Formulário de Referência da Petrobras reproduzido pela Latibex](https://www.latibex.com/docs/Documentos/LED/2022/12/14/TRACN_20220401_123519_B11_122574_20220101_DOC001.pdf). A moeda e a estrutura de capital sofreram mudanças históricas; não converter o valor nominal diretamente para reais nem tratá-lo como cotação histórica.

Para determinar o preço original de emissão, será necessário localizar prospecto/anúncio de distribuição ou documento primário que identifique preço efetivo e data, esclarecer se a referência pretendida é a constituição/subscrição inicial de 1953 ou a primeira oferta pública de mercado, e reconciliar todos os eventos societários relevantes. O registo de grupamentos, desdobramentos e bonificações não cobre sozinho aumentos de capital, subscrições, cisões, incorporações, alterações de classe e dividendos.

## Fórmula de normalização

Para um evento com fator total `f = ações após / ações antes`, converter preço histórico para unidades atuais dividindo pelo produto dos fatores aplicáveis posteriores à data do preço. Isto ajusta quantidade/unidade; não calcula retorno total com dividendos.

## Fontes

1. [B3 — Eventos corporativos de PETR](https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/9512/PETR/corporate-actions?language=pt-BR) — página consultada em 2026-10-13.
2. [Relatório anual Petrobras 1993 — cópia em arquivo AEPET](https://bibliotecadigital.aepet.org.br/wp-content/uploads/2024/01/Relatorio-anual-1993.pdf) e [Decreto de 02/07/1993 — Senado Federal](https://legis.senado.leg.br/norma/375645/publicacao/15655719).
3. [Petrobras Form 20-F — SEC, evento de 2005](https://www.sec.gov/Archives/edgar/data/1119639/000095012307009305/y36368a1e20vfza.htm).
4. [Petrobras — documento arquivado na SEC sobre o ajuste de 2008](https://www.sec.gov/Archives/edgar/data/831001/000119312510139139/dfwp.htm).
5. [Lei nº 2.004/1953 — Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/lei/1950-1959/lei-2004-3-outubro-1953-366242-publicacaooriginal-1-pl.html) — capital inicial legal, não prova de preço de IPO.
6. [Formulário de Referência Petrobras — Latibex](https://www.latibex.com/docs/Documentos/LED/2022/12/14/TRACN_20220401_123519_B11_122574_20220101_DOC001.pdf) — listagem em 1956 e primeiro negócio em 1957.

## Limitações e próxima etapa

- A cobertura oficial consultada não estabelece que a série histórica esteja completa desde a origem.
- A data efetiva da bonificação de 1994, a data efetiva do grupamento de 2000 e a data ex do desdobramento de 2008 devem ser corroboradas com documentos históricos específicos do emissor antes de usar os fatores em cálculo auditável de retorno.
- Próxima etapa: confirmar em fonte primária as datas ex de 1993, 1994 e 2000; pesquisar o preço do primeiro negócio de dezembro de 1957 em arquivo histórico da bolsa; e continuar a procurar o documento de preço original de emissão/subscrição.
