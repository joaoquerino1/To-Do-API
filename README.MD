# To-Do API
API REST para o gerenciamento de tarefas. 

## Tecnologias utilizadas
- Python 3 + Flask
- JSON para persistência

## Como rodar
1. Clone o repositório
2. Instale dependências: pip install -r requirements.txt
3. Rode: python app.py
4. Acesse: http://localhost:5000

## Endpoints
- GET    /tarefas
- POST   /tarefas
- PUT    /tarefas/id
- DELETE /tarefas/id


## 🚀 Próximos Passos (Roadmap)

Este projeto está em constante evolução. As próximas funcionalidades que pretendo implementar são:

- [ ] **Persistência em Banco de Dados:** Substituir o arquivo JSON pelo PostgreSQL utilizando SQLAlchemy (ORM).
- [ ] **Autenticação:** Implementar login de usuários e proteção de rotas com JWT (JSON Web Tokens).
- [ ] **Categorização:** Adicionar etiquetas (tags) e categorias para organizar melhor as tarefas.
- [ ] **Datas e Prazos:** Incluir campos de data de vencimento e lembretes.
- [ ] **Filtros Avançados:** Filtros por data, prioridade e busca por texto na interface.
- [ ] **Documentação:** Adicionar Swagger/OpenAPI para documentar os endpoints da API de forma interativa.
