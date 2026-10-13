# GRUPAMENTOS — histórico e verificação

**ID:** STOCKS-EVENTOS-GRUPAMENTOS-001 · **Versão:** 1.0.0  
**Finalidade:** centralizar eventos confirmados de grupamento (inplit / reverse split) e evidências por ativo.

## Regras
- Um grupamento só é **VERIFICADO** quando existe evidência primária identificável: comunicado/aviso ao acionista, ata, documento do RI, registro da B3 ou documento regulatório aplicável.
- Resultados de pesquisa, notícias secundárias e snippets são pistas, não prova.
- Registar ticker/classe, razão social, proporção, datas, fonte específica e verificador.
- Preservar eventos históricos; correções geram nova revisão, sem apagar silenciosamente a evidência anterior.
- A ausência de evento encontrado não prova que nunca houve grupamento. Usar `UNKNOWN` quando a cobertura histórica não for suficiente.

## Arquivos
- `registros.json`: registo canónico dos eventos verificados de grupamento.
- `../VERIFICADOR_EVENTOS_SOCIETARIOS/README.md`: execução e estados do verificador.
- Relatórios gerados: `../VERIFICADOR_EVENTOS_SOCIETARIOS/relatorios/` (não guardar dados transitórios sem necessidade).

## Proporção
Guardar `new_shares_per_old_share`: quantidade de ações após o evento por cada ação anterior. Exemplo: 1 ação nova para 10 antigas = `0.1`. A validação final deve confirmar a proporção no documento oficial.