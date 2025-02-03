# Gerenciador de Tarefas - API

Esta API permite a criação, leitura, atualização e exclusão de tarefas, além de filtrar tarefas com base no status.

## Tecnologias Utilizadas
- Python
- Django REST Framework
- SQLite (pode ser substituído por outro banco de dados)

## Instalação e Configuração
### 1. Clonar o repositório


### 2. Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv\Scripts\activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados
```bash
python manage.py migrate
```

### 5. Rodar o servidor localmente
```bash
python manage.py runserver
```
A API estará disponível em `http://127.0.0.1:8000/`.

## Endpoints
### Criar uma tarefa (POST /tarefas/)


### Listar todas as tarefas (GET /tarefas/)


### Buscar uma tarefa por ID (GET /tarefas/{id}/)


### Atualizar uma tarefa (PUT /tarefas/{id}/)


### Excluir uma tarefa (DELETE /tarefas/{id}/)


### Filtrar tarefas por status (GET /tarefas/?status=pendente)
