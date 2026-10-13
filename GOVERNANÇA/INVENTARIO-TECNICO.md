# Inventário técnico inicial — STOCKS

**Data da inspeção:** 2026-10-13  
**Branch examinada:** `main`  
**Estado:** Inventário documental parcial, com caminhos verificados individualmente. Não equivale a auditoria integral de todo o repositório.

## 1. Resumo executivo

A inspeção confirmou a documentação de governação, a estrutura `AÇÕES/`, o catálogo de fontes e a pasta-modelo por ticker. Não foram encontrados, nos caminhos técnicos verificados, o registo `registry/acoes.json`, o script `scripts/criar_acao.py` ou o workflow `.github/workflows/criar-pasta-acao.yml`. Também não foi identificado, nesta inspeção, um pipeline de ingestão, uma base de dados de mercado ou automação WATCHDOG local ao STOCKS.

**Conclusão:** a base atual é sobretudo documental. A automação de criação de dossiers, o inventário de dados e a integração de monitorização continuam por implementar ou por localizar e verificar.

## 2. Inventário confirmado

| Ativo | Caminho | Estado observado | Observação |
|---|---|---|---|
| README principal | `README.md` | EXISTE | Liga à governança e à área AÇÕES. |
| Instruções de análise por ticker | `AÇÕES/README.md` | EXISTE | Define convenção de criação, índice e limitação cross-chat. |
| Catálogo de fontes | `AÇÕES/FONTES/README.md` | EXISTE | Lista repositórios e fontes institucionais de referência. |
| Modelo de dossier | `AÇÕES/_MODELO_ACAO/README.md` | EXISTE | Template; não é uma ação real. |
| Perfil fundamental | `AÇÕES/_MODELO_ACAO/perfil.md` | PREVISTO NO MODELO | Estrutura de identificação e contexto do emissor. |
| Análise fundamentalista | `AÇÕES/_MODELO_ACAO/fundamentalista.md` | PREVISTO NO MODELO | Análise de demonstrações e valuation. |
| Técnica e fluxo | `AÇÕES/_MODELO_ACAO/tecnica-e-fluxo.md` | PREVISTO NO MODELO | Indicadores e comportamento de mercado. |
| Eventos e catalisadores | `AÇÕES/_MODELO_ACAO/eventos-e-catalisadores.md` | PREVISTO NO MODELO | Eventos e catalisadores. |
| Riscos | `AÇÕES/_MODELO_ACAO/riscos.md` | PREVISTO NO MODELO | Riscos e condições de invalidação. |
| Fontes por ticker | `AÇÕES/_MODELO_ACAO/fontes.md` | EXISTE | Define linhagem e limitações das fontes. |
| Governança local | `GOVERNANÇA/` | EXISTE | Documentação, matriz de controlos e registo de adoção. |

Os ficheiros individuais do modelo são documentação de referência, não dados de uma empresa nem prova de que exista análise iniciada.

## 3. Componentes não encontrados nos caminhos verificados

| Componente | Caminho verificado | Resultado | Consequência |
|---|---|---|---|
| Registo central de tickers | `registry/acoes.json` | NÃO ENCONTRADO | Sem índice de máquina confirmado. |
| Script de criação | `scripts/criar_acao.py` | NÃO ENCONTRADO | Criação ainda não automatizada por este script. |
| Workflow de criação | `.github/workflows/criar-pasta-acao.yml` | NÃO ENCONTRADO | Não há workflow de criação confirmado. |
| Workflow de testes local | `.github/workflows/` | NÃO CONFIRMADO | Inventariar os workflows completos quando a árvore puder ser consultada. |
| Dataset local de mercado | Caminho não identificado | NÃO IDENTIFICADO | Não assumir ingestão local ou atualidade de dados. |
| Motor analítico / backtest | Caminho não identificado | NÃO IDENTIFICADO | Não assumir cálculos reproduzíveis implementados neste repo. |
| Integração WATCHDOG | Caminho não identificado | NÃO IDENTIFICADA | WATCHDOG não pode ser declarado ativo no STOCKS. |
| Dossier de ticker real | `AÇÕES/<TICKER>/` | NÃO IDENTIFICADO NA INSPEÇÃO | A pasta-modelo não conta como ativo analisado. |

`NÃO ENCONTRADO` significa que o caminho específico consultado devolveu inexistente. `NÃO IDENTIFICADO` significa que não foi localizada evidência na inspeção disponível; não é uma afirmação de inexistência universal.

## 4. Classificação preliminar de risco

A classificação abaixo é inicial e deve ser confirmada por fluxo; não substitui avaliação legal ou regulatória.

| Fluxo / ativo | Nível preliminar | Justificação | Controlos prioritários |
|---|---|---|---|
| Documentação e templates | A — Essencial | Conteúdo estático e reversível. | Revisão, histórico, links e consistência. |
| Catálogo de fontes | B — Normal | Fonte incorreta pode contaminar análises. | Revisão periódica, classificação de fonte e URL/data de acesso por análise. |
| Dossiers de empresas | C — Elevado | Pode influenciar decisões financeiras. | Fontes primárias, unidade/período, revisão independente proporcional e riscos explícitos. |
| Ingestão de preços/demonstrações (quando criada) | C — Elevado | Dados incorretos/desatualizados podem propagar-se a métricas. | Linhagem, schema, completude, atualidade, reconciliação e logs. |
| Backtest/sinal automatizado (se vier a existir) | C — Elevado; rever para D conforme uso | Risco de viés, erro de cálculo e ação financeira indevida. | Dados/versionamento, custos, prevenção de leakage, limites e aprovação humana. |
| Publicação/automação GitHub | B — Normal | Risco de corrupção do histórico, concorrência ou exposição de secrets. | Menor privilégio, idempotência, testes, revisão e rollback. |
| WATCHDOG/alertas | C — Elevado se usado para controlos críticos | Falsa sensação de monitorização se não houver supervisão/ACK. | Estados UNKNOWN, heartbeat independente, testes de alerta e owner. |

## 5. Ownership

Não foi encontrada evidência documental suficiente para atribuir papéis operacionais individuais a todos os fluxos. Não inferir owner apenas pelo nome do proprietário do repositório.

| Domínio | Owner atual | Estado | Próxima evidência necessária |
|---|---|---|---|
| Governança STOCKS | A designar formalmente | UNKNOWN | Aprovação/decisão no registo de adoção. |
| Dados de mercado | A designar | UNKNOWN | Inventário de fontes, pipeline e responsável de dados. |
| Análise por ticker | A designar por dossier | UNKNOWN | Campo de responsável e data de revisão preenchidos. |
| Scripts/workflows | A designar | UNKNOWN | RACI por automação e permissões. |
| Segurança/privacidade | A designar conforme risco | UNKNOWN | Avaliação e mandato explícitos. |
| Operações/WATCHDOG | A designar | UNKNOWN | Owner, runbook, escalonamento e teste de alertas. |

## 6. Limitações da inspeção

A pesquisa por código do GitHub não devolveu resultados para STOCKS e a consulta da árvore completa não ficou disponível nesta inspeção. Por isso, a verificação foi feita por leitura de ficheiros conhecidos e consultas de caminhos específicos. O inventário é útil para identificar lacunas confirmadas, mas ainda não é um mapa exaustivo de todos os ficheiros e workflows.

## 7. Próximo passo de auditoria

Obter uma listagem completa da árvore `main`, examinar todos os ficheiros `.github/workflows/`, scripts e manifests; confirmar eventuais artefactos de dados; executar testes disponíveis; e atualizar esta tabela com SHA, URLs e resultados. Até lá, componentes não encontrados ficam `UNKNOWN`/`NÃO IDENTIFICADO`, não `PASS`.
