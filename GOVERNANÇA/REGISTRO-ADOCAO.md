# Registo de adoção da governança — STOCKS

**Data de criação:** 2026-10-13  
**Referência principal:** https://github.com/carlos-andrade/GOVERNANCA  
**Estado geral:** DOCUMENTAÇÃO LOCAL INICIADA; ADOÇÃO OPERACIONAL NÃO CERTIFICADA.

## Fonte-mãe consultada

Consultados o ramo `main`, árvore do repositório, README, Constituição, modelo operacional, papéis, política de decisões e ciclo de vida/gates. A estrutura consultada também identifica políticas de dados/IA, segurança/privacidade, operações/resiliência, templates, registos de estado e WATCHDOG.

Na consulta, o README da fonte-mãe informava estado de finalização e 80% comprovado, com pendências relacionadas com aprovação de limites de atualidade, adoção transversal, supervisão independente e testes operacionais de alertas/SLA. Estes são estados da fonte-mãe na data consultada e devem ser reconfirmados; não são automaticamente estados do STOCKS.

## Entregue nesta camada

- Estrutura documental local e ligações à fonte normativa.
- Princípios de integridade, hierarquia documental e risco proporcional.
- Papéis e RACI mínimos.
- Gates G0–G6 com evidências exigidas.
- Política de dados, fontes, linhagem e qualidade para análise de ações.
- Políticas de risco, segurança, privacidade, decisões, alterações, validação, release e continuidade.
- Regra explícita de não presumir monitorização ativa.
- Matriz de controlos com estados iniciais conservadores.

## Não comprovado

- Aprovação formal dos documentos locais.
- Mapeamento RACI de todos os fluxos STOCKS.
- Auditoria de segurança e permissões.
- Testes de qualidade para cada ingestão, dataset e cálculo.
- Integração/execução do WATCHDOG no STOCKS.
- Configuração/teste de canais, heartbeat independente, ACK/SLA.
- Teste de restauração de backup e continuidade.
- Gates automáticos e validação de release.
- Certificação ou conformidade legal/regulatória.

## Próximas ações

1. Rever a estrutura local contra as necessidades reais do STOCKS e documentos aplicáveis da fonte-mãe.
2. Obter aprovação para esta adaptação e definir owners por domínio.
3. Inventariar pipelines, datasets, scripts, análises e workflows existentes.
4. Associar cada fluxo a risco, dados, evidências, testes, owner e recuperação.
5. Implementar primeiro os controlos de maior risco e as lacunas comprovadas.
6. Adotar WATCHDOG somente após inventário, configuração, testes e aceitação local.
7. Atualizar estados apenas com evidência rastreável.

## Histórico

| Data | Alteração | Estado |
|---|---|---|
| 2026-10-13 | Estrutura documental local e matriz de controlos iniciais | Publicação dos ficheiros registada via commits; validação pós-publicação a executar. |
