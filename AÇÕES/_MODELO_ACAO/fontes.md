# Fontes e linhagem — <TICKER>

Este ficheiro regista as fontes efetivamente utilizadas na análise de cada ação. Os repositórios de projetos são referências de processo e dados; os sites oficiais são fontes institucionais. A inclusão nesta lista não significa que todos os dados de uma fonte tenham sido auditados ou validados.

## Fontes de referência do projeto

| Fonte | URL | Utilização prevista | Natureza | Limitações / controlos |
|---|---|---|---|---|
| GOVERNANCA | https://github.com/carlos-andrade/GOVERNANCA | Regras de governança, evidências, rastreabilidade e critérios de validação do projeto. | Governança do projeto | Confirmar a versão/regra aplicável antes de declarar conformidade. |
| B3 — repositório do projeto | https://github.com/carlos-andrade/B3 | Consultar processos e artefactos internos de dados de mercado, ingestão e histórico, incluindo COTAHIST/BDI quando aplicável. | Repositório de projeto | Verificar período, integridade, origem e estado de validação do artefacto utilizado. |
| BLOOMBERG_MAIL | https://github.com/carlos-andrade/BLOOMBERG_MAIL | Consultar processos de ingestão e organização de informação recebida por e-mail e evidências relacionadas com dados de mercado. | Repositório de projeto | Não tratar automaticamente o conteúdo de e-mails como fonte oficial ou dado validado. |
| DECIO-BAZIN | https://github.com/carlos-andrade/DECIO-BAZIN | Referência complementar para análise orientada a investimento e critérios documentados no projeto. | Repositório de projeto / metodologia | Distinguir metodologia, opinião e cálculo dos dados primários do emissor. |

## Fontes institucionais oficiais

| Fonte | URL | Utilização prevista | Natureza | Limitações / controlos |
|---|---|---|---|---|
| B3 — Brasil, Bolsa, Balcão | https://www.b3.com.br/ | Consultar informação institucional de mercado, instrumentos, cotações, dados históricos e documentos disponibilizados pela bolsa, conforme disponibilidade. | Fonte institucional primária | Registar produto, período, horário, unidade e eventuais atrasos ou restrições. |
| CVM — Comissão de Valores Mobiliários | https://www.gov.br/cvm/ | Consultar documentos regulatórios e divulgações oficiais de emissores, incluindo demonstrações financeiras e fatos relevantes, quando disponíveis. | Regulador / fonte oficial | Confirmar emissor, documento, data de divulgação e período contabilístico. |
| Relações com Investidores (RI) do emissor | A preencher para cada emissor | Consultar resultados, apresentações, comunicados, políticas de dividendos e outros documentos publicados pelo próprio emissor. | Fonte primária do emissor | Guardar o URL específico do documento, data de publicação e período coberto. |

## Registo obrigatório por análise

Para cada fonte realmente utilizada, preencher os campos abaixo na tabela de evidências da análise individual:

| Campo | Regra |
|---|---|
| Fonte / documento | Identificar a entidade e o documento específico. |
| URL | Guardar o endereço direto da página ou ficheiro, quando possível. |
| Data de publicação | Registar a data indicada pela fonte; usar “não indicada” se ausente. |
| Data de acesso (UTC) | Registar a data efetiva de consulta. |
| Período coberto | Indicar o período económico ou intervalo temporal dos dados. |
| Tipo | Classificar como oficial/primária, derivada, estimativa ou opinião. |
| Limitações | Anotar atrasos, dados em falta, alterações metodológicas ou outras ressalvas. |

## Regras de evidência

- Priorizar B3, CVM, demonstrações financeiras auditadas, comunicados oficiais e RI do emissor para factos sobre a empresa.
- Usar os repositórios de projeto para localizar processos, dados e evidências internas, sem os confundir com fontes institucionais.
- Registar URL, data de acesso e período de referência para os dados efetivamente usados.
- Distinguir preço em tempo real, atrasado, de fecho e histórico; identificar moeda, unidade, fuso horário e data/hora relevantes.
- Distinguir claramente dados oficiais, dados derivados, estimativas e opiniões.
- Sinalizar divergências entre fontes e explicar qual foi priorizada e porquê.
- Não inventar dados ausentes nem declarar validação sem evidência verificável.
- Não armazenar credenciais, dados pessoais desnecessários ou conteúdo integral protegido por direitos de autor.
