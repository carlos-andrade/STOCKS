# DESDOBRAMENTOS — histórico e verificação

**ID:** STOCKS-EVENTOS-DESDOBRAMENTOS-001 · **Versão:** 1.0.0  
**Finalidade:** centralizar eventos confirmados de desdobramento (split) e evidências por ativo.

## Regras
- Um desdobramento só é **VERIFICADO** quando existe evidência primária identificável: comunicado/aviso ao acionista, ata, documento do RI, registro da B3 ou documento regulatório aplicável.
- Resultados de pesquisa, notícias secundárias e snippets são pistas, não prova.
- Registar ticker/classe, razão social, proporção, datas, fonte específica e verificador.
- Preservar eventos históricos; correções geram nova revisão, sem apagar silenciosamente a evidência anterior.
- A ausência de evento encontrado não prova que nunca houve desdobramento. Usar `UNKNOWN` quando a cobertura histórica não for suficiente.

## Arquivos
- `registros.json`: registo canónico dos eventos verificados de desdobramento.
- `../VERIFICADOR_EVENTOS_SOCIETARIOS/README.md`: execução e estados do verificador.

## Proporção
Guardar `new_shares_per_old_share`: quantidade de ações após o evento por cada ação anterior. Exemplo: 5 ações novas para cada ação antiga = `5.0`. A validação final deve confirmar a proporção no documento oficial.