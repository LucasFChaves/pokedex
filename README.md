# pokedex
#  Catálogo de Pokémons - Carvalho

Este é um sistema web criado para o pesquisador Carvalho, que precisa cadastrar e gerenciar Pokémons de forma simples e rápida.

O sistema é dividido em duas partes:

- Frontend: Interface web feita com React.
- Backend: API REST feita com Flask (Python) e banco de dados SQLite3.

---

# Funcionalidades

# Frontend (React)

-  Listagem completa dos Pokémons com:
  - Código
  - Nome
  - Tipo Primário
  - Tipo Secundário
  - Botões de **Editar** e **Excluir**
-  Filtro por **nome**
-  Filtro por **tipo**
-  Botão para **adicionar novo Pokémon**
-  Botão para **gerenciar tipos**
-  Página para adicionar, editar e excluir tipos de Pokémon

# Backend (Flask + SQLite)

-  API REST para:
  - Listar Pokémons
  - Adicionar, editar e excluir Pokémons
  - Gerenciar tipos (listar, adicionar, editar, excluir)
-  Banco de dados SQLite com tabelas `pokemons` e `tipos`
-  Endpoints protegidos com verificação básica de dados

---

# Requisitos

# Frontend

- Node.js (versão 14 ou superior)
- npm ou yarn

# Backend

- Python 3.8+
- pip (gerenciador de pacotes)

---

# Como rodar o projeto

# Backend

1. Acesse a pasta do backend:

bash
cd backend

2. Instale as dependências:

bash
pip install -r requirements.txt

3. Inicie o servidor FLASK:

bash
python app.py

O backend será iniciado em:
 http://localhost:5000

# Frontend

1. Acesse a pasta do frontend:

bash
cd frontend

2. Instale as dependências:

bash
npm install

3. Inicie o servidor de desenvolvimento:

bash
npm start

A interface estará disponível em:
 http://localhost:3000

Certifique-se de que o frontend esteja configurado para se comunicar com o backend em http://localhost:5000.
