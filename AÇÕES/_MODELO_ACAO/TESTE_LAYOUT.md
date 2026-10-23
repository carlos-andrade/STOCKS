<!-- STOCKS | ID: STOCKS-ACAO-LAYOUT-TEST-001 | Versão: 1.0.0 | Estado: CHECKLIST -->
# Checklist de teste do layout de ações

## Objetivo
Validar que o modelo pode ser copiado para qualquer ação da B3 sem perder rastreabilidade, consistência ou distinção entre dados confirmados e pendentes.

## Testes de aceitação
- [ ] Pasta criada em AÇÕES/<TICKER>/, sem usar a pasta-modelo como dossiê real.
- [ ] Ticker, emissor e classe confirmados em fonte oficial.
- [ ] Identificadores (CNPJ/ISIN) registados ou marcados como não localizados.
- [ ] Todos os ficheiros do modelo criados.
- [ ] Fontes têm URL exata, tipo, data de publicação/acesso, período e limitações.
- [ ] Factos, cálculos, estimativas, inferências e opiniões estão separados.
- [ ] Verificador de eventos societários executado; comando, estado e relatório registados.
- [ ] Eventos com fonte primária e datas/fatores avaliados separadamente.
- [ ] Eventos pendentes não utilizados silenciosamente em ajustes de preços/retornos.
- [ ] Série de preços tem fonte, período, timezone, unidade e estado de ajuste documentados.
- [ ] Indicadores têm definição/fórmula, parâmetros, inputs e data de referência.
- [ ] Riscos e condições de invalidação registados.
- [ ] Snapshot inicial datado guardado em historico/AAAA-MM-DD.md.
- [ ] Índice AÇÕES/README.md e registry/acoes.json atualizados quando aplicável.
- [ ] Limitações e pendências explícitas; nenhum dado ausente tratado como zero ou como prova de inexistência.
- [ ] Revisão por Pull Request e validações CI concluídas antes de integrar na main.

## Matriz de estados
| Estado | Significado |
|---|---|
| NÃO INICIADA | Modelo copiado, pesquisa ainda não iniciada |
| EM ANÁLISE | Pesquisa em curso, pendências abertas |
| PARCIAL | Existe análise útil, mas há lacunas materiais |
| VALIDADA | Critérios de validação definidos para o escopo foram satisfeitos; não significa cobertura absoluta |
| BLOQUEADA | Uma lacuna material impede a conclusão pretendida |

## Regra de teste
O primeiro teste real após a publicação deve usar um ticker escolhido explicitamente para análise. O dossiê PETR4 serve como caso de regressão para eventos históricos, não como prova de que o layout foi validado para todos os emissores.
