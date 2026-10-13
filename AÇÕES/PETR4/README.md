# PETR4 — Dossiê de eventos societários e origem do preço

**Emissor:** Petróleo Brasileiro S.A. — Petrobras  
**Ticker analisado:** PETR4 (ação preferencial)  
**Data da pesquisa:** 2026-10-13  
**Estado da cobertura histórica:** PARCIAL — não equivale a reconstrução completa de capital nem a determinação do preço original de IPO.

## Eventos identificados na tabela oficial da B3

| Último dia indicado para negociar com direito (B3) | Evento | Fator total de ações após/antes | Data efetiva/ex-date | Estado |
|---|---|---:|---|---|
| 25/03/1994 | Bonificação de 33,333333333% | 1,33333333333 | 28/03/1994 inferida; pendente de confirmação | PENDENTE |
| 21/06/2000 | Grupamento 100:1 | 0,01 | 22/06/2000 inferida; pendente de confirmação | PENDENTE |
| 25/04/2008 | Desdobramento de 100% (uma ação adicional por ação existente) | 2,0 | A companhia reporta efeito a partir de 25/04/2008; ex-date não confirmado | Evento/fator verificados; ex-date pendente |

Fonte dos eventos e fatores: [B3 — Eventos corporativos de PETR](https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/9512/PETR/corporate-actions?language=pt-BR). A coluna da B3 é “Negócios com até”; ela identifica o último dia com direito, não deve ser copiada automaticamente para o campo de data ex. Para 1994 e 2000, a data efetiva indicada acima é uma inferência do próximo dia útil, não uma data confirmada pela fonte. Para o desdobramento de 2008, a demonstração financeira da companhia descreve a operação como efetiva a partir de 25/04/2008; a data ex usada para ajuste da cotação continua por confirmar.

O fator foi normalizado para o contrato de dados STOCKS: ações totais após o evento divididas pelas ações antes do evento. A B3 exibe “100” para o desdobramento de 2008, significando uma ação adicional por ação existente, não fator total 100x.
## Candidatos ainda não confirmados

- **05/07/1993 — alegado desdobramento 80:1:** não foi confirmado na tabela consultada da B3 nem foi localizada, nesta revisão, evidência primária específica. Não incorporar como evento confirmado.
- **2005 — alegado desdobramento 4:1:** não foi confirmado na tabela consultada da B3 nem foi localizada, nesta revisão, evidência primária específica. Não incorporar como evento confirmado.

Estes pontos permanecem pendentes de pesquisa em documentos históricos da companhia/CVM; a ausência na tabela atual da B3 não prova que nunca ocorreram.

## Preço original de emissão / IPO

**Estado: UNKNOWN — preço original de IPO não estabelecido.** Não confundir valor nominal legal, preço de subscrição, preço de oferta pública e primeira cotação observada.

A [Lei nº 2.004, de 3 de outubro de 1953, art. 9º](https://www2.camara.leg.br/legin/fed/lei/1950-1959/lei-2004-3-outubro-1953-366242-publicacaooriginal-1-pl.html) definiu capital inicial de Cr$ 4.000.000.000,00 dividido em 20.000.000 ações ordinárias nominativas de Cr$ 200,00 cada. Esse valor legal nominal de 1953 **não comprova o preço de uma oferta pública inicial nem o preço de negociação da PETR4**. A moeda e a estrutura de capital sofreram mudanças históricas; não converter este valor diretamente para reais nem tratá-lo como cotação histórica.

Para determinar o preço original de emissão, será necessário localizar prospecto/anúncio de distribuição ou documento primário que identifique preço efetivo e data, esclarecer se a referência pretendida é a constituição/subscrição inicial de 1953 ou a primeira oferta pública de mercado, e reconciliar todos os eventos societários relevantes. O registo de grupamentos, desdobramentos e bonificações não cobre sozinho aumentos de capital, subscrições, cisões, incorporações, alterações de classe e dividendos.

## Fórmula de normalização

Para um evento com fator total `f = ações após / ações antes`, converter preço histórico para unidades atuais dividindo pelo produto dos fatores aplicáveis posteriores à data do preço. Isto ajusta quantidade/unidade; não calcula retorno total com dividendos.

## Fontes

1. [B3 — Eventos corporativos de PETR](https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/9512/PETR/corporate-actions?language=pt-BR) — página consultada em 2026-10-13.
2. [Lei nº 2.004/1953 — Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/lei/1950-1959/lei-2004-3-outubro-1953-366242-publicacaooriginal-1-pl.html) — capital inicial legal, não prova de preço de IPO.
3. [CVM — Informações de companhias](https://www.gov.br/cvm/pt-br/assuntos/regulados/consultas-por-participante/companhias) — fonte institucional para continuação da pesquisa documental.

## Limitações e próxima etapa

- A cobertura oficial consultada não estabelece que a série histórica esteja completa desde a origem.
- A data efetiva da bonificação de 1994, a data efetiva do grupamento de 2000 e a data ex do desdobramento de 2008 devem ser corroboradas com documentos históricos específicos do emissor antes de usar os fatores em cálculo auditável de retorno.
- Próxima etapa: localizar comunicados/atas e documentos CVM históricos para os candidatos de 1993 e 2005, confirmar a data operacional da bonificação de 1994 e pesquisar o preço de emissão original em documento primário.
