# Registo de inspeção técnica — 2026-10-13

**Repositório:** `carlos-andrade/STOCKS`  
**Branch:** `main`  
**Objetivo:** iniciar inventário de workflows, scripts, dados e estruturas de análise antes de integrar WATCHDOG.

## Verificações concluídas

| Caminho | Resultado | Evidência consultada |
|---|---|---|
| `README.md` | Encontrado | https://github.com/carlos-andrade/STOCKS/blob/main/README.md |
| `AÇÕES/README.md` | Encontrado | https://github.com/carlos-andrade/STOCKS/blob/main/A%C3%87%C3%95ES/README.md |
| `AÇÕES/FONTES/README.md` | Encontrado | https://github.com/carlos-andrade/STOCKS/blob/main/A%C3%87%C3%95ES/FONTES/README.md |
| `AÇÕES/_MODELO_ACAO/README.md` | Encontrado | https://github.com/carlos-andrade/STOCKS/blob/main/A%C3%87%C3%95ES/_MODELO_ACAO/README.md |
| `AÇÕES/_MODELO_ACAO/fontes.md` | Encontrado | https://github.com/carlos-andrade/STOCKS/blob/main/A%C3%87%C3%95ES/_MODELO_ACAO/fontes.md |
| `registry/acoes.json` | 404 / não encontrado | Consulta direta do caminho no branch `main`. |
| `scripts/criar_acao.py` | 404 / não encontrado | Consulta direta do caminho no branch `main`. |
| `.github/workflows/criar-pasta-acao.yml` | 404 / não encontrado | Consulta direta do caminho no branch `main`. |

## Resultado da inspeção estrutural

A listagem da raiz e das pastas `AÇÕES/`, `AÇÕES/_MODELO_ACAO/`, `AÇÕES/FONTES/` e `GOVERNANÇA/` foi obtida. A raiz da branch `main` contém `AÇÕES/`, `GOVERNANÇA/`, `LICENSE` e `README.md`; não existem diretórios `.github/`, `scripts/` ou `registry/` na raiz observada. A pesquisa de código não devolveu resultados. Não foram executados testes de código nem auditadas permissões, histórico completo ou dados externos.

## Decisão de controlo

Não ativar nem declarar WATCHDOG no STOCKS como ativo. Primeiro completar inventário, definir ownership e limites, validar contratos de dados e obter testes. Integração inicial deve ser read-only, com estado `UNKNOWN` para qualquer dependência sem evidência.

## Próxima revisão

Após obtenção da árvore integral e revisão de todos os workflows/scripts. Atualizar este registo com caminhos, SHA, resultados de testes e responsáveis efetivamente designados.
