# <TICKER> — Dossiê de análise

> Copiar esta estrutura para `AÇÕES/<TICKER>/` quando uma nova ação for citada para análise. Substituir todos os campos entre sinais angulares.

## Identificação
- Ticker:
- Empresa:
- CNPJ:
- Segmento / setor:
- Classe do ativo:
- Bolsa / mercado:
- Moeda-base: BRL
- ISIN:
- Website de RI:
- Fontes oficiais:
- Estado da análise: NÃO INICIADA
- Última revisão (UTC):
- Responsável pela revisão:

## Arquivos desta pasta
- `perfil.md` — negócio, setor, governança, riscos e tese.
- `fundamentalista.md` — demonstrações financeiras, indicadores e valuation.
- `tecnica-e-fluxo.md` — preço, volume, VWAP, volatilidade, fluxo e níveis técnicos.
- `eventos-e-catalisadores.md` — resultados, fatos relevantes, calendário e eventos.
- `riscos.md` — mapa de riscos, cenários e condições de invalidação.
- `historico/AAAA-MM-DD.md` — snapshots de análise datados, sem apagar versões anteriores.
- `fontes.md` — fontes, URLs, data de acesso, período coberto e limitações.

## Protocolo
1. Validar identidade do ativo em fonte oficial (B3, CVM e RI da companhia).
2. Separar fatos reportados, estimativas, hipóteses e opinião.
3. Informar data de referência, moeda, unidade, período e origem de cada número.
4. Não apresentar dados atrasados como atuais nem estimativas como fatos.
5. Não produzir recomendação de compra/venda sem tese, horizonte, valuation, riscos e cenários.
6. Registrar divergências, dados ausentes e limitações.
7. Atualizar `registry/acoes.json` e o índice de `AÇÕES/README.md` ao cadastrar o ticker.

Esta estrutura é inspirada funcionalmente em ferramentas de gestão de carteira e análise de ações, sem copiar código, textos, identidade visual ou conteúdo proprietário do MyStocks.
