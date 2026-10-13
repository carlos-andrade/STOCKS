<!-- STOCKS | ID: STOCKS-ACAO-MODELO-001 | Versão: 1.1.0 | Estado: MODELO -->
# <TICKER> — Dossiê de análise

Copiar este modelo para `AÇÕES/<TICKER>/` quando uma nova ação for selecionada para análise. Não editar os ficheiros de modelo para guardar dados reais. Substituir todos os campos de exemplo e manter explícitas as lacunas.

## Identificação
- Ticker e classe:
- Empresa / nome legal:
- CNPJ:
- ISIN:
- Segmento / setor:
- Bolsa / mercado:
- Moeda-base: BRL
- Website de Relações com Investidores:
- Estado da análise: NÃO INICIADA
- Data de referência:
- Última revisão (UTC):
- Responsável/revisor:

## Conjunto obrigatório de ficheiros
- `perfil.md` — negócio, setor, capital, governança e tese.
- `fundamentalista.md` — demonstrações financeiras, indicadores, metodologia e valuation.
- `tecnica-e-fluxo.md` — integridade da série, preço, volume, volatilidade e cenários.
- `eventos-e-catalisadores.md` — eventos societários, datas, fatores e catalisadores.
- `riscos.md` — mapa de riscos, cenários de stress e condições de bloqueio.
- `fontes.md` — fontes utilizadas, evidências, datas, períodos e limitações.
- `historico/README.md` — regra de snapshots imutáveis por data.
- `historico/AAAA-MM-DD.md` — snapshot da análise em cada data de revisão.
- `TESTE_LAYOUT.md` — checklist de aceitação para confirmar a aplicação correta do modelo.

## Protocolo obrigatório
1. Confirmar ticker, emissor e classe em fonte oficial.
2. Executar o verificador de eventos societários antes de calcular retornos históricos ou comparar preços atravessando eventos.
3. Separar factos reportados, cálculos, estimativas, inferências e opinião.
4. Informar data de referência, moeda, unidade, período e origem de cada número.
5. Registar URL exata, data de publicação quando disponível, data de acesso, período coberto e limitações.
6. Não apresentar dados atrasados como atuais, estimativas como factos ou dados ausentes como zero.
7. Não marcar evento como verificado com base apenas numa fonte secundária.
8. Não apagar snapshots anteriores; preservar histórico e evidência de alterações.
9. Atualizar `registry/acoes.json` e `AÇÕES/README.md` quando o ticker for cadastrado.
10. Submeter alterações por Pull Request e cumprir a governança central antes de integrar na `main`.

## Estados padronizados
- **NÃO INICIADA:** o modelo foi copiado, sem análise substantiva.
- **EM ANÁLISE:** pesquisa em curso.
- **PARCIAL:** análise útil com lacunas materiais explicitadas.
- **VALIDADA:** os critérios de validação do escopo foram satisfeitos; não significa completude absoluta.
- **BLOQUEADA:** uma lacuna material impede a conclusão pretendida.

## Governança e fontes de referência
A governança central do projeto é definida em https://github.com/carlos-andrade/GOVERNANCA. Fontes de referência obrigatórias do STOCKS estão catalogadas em [FONTES](../FONTES/README.md), incluindo os repositórios GOVERNANCA, B3, BLOOMBERG_MAIL e DECIO-BAZIN, além dos sites oficiais da B3 e da CVM.

Este layout é uma estrutura funcional interna. Não copia código, textos, identidade visual ou conteúdo proprietário de terceiros.
