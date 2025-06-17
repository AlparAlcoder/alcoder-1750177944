# Task Management API

## Descrição geral

Este é um exemplo simples de uma API de gerenciamento de tarefas usando FastAPI. A API permite a criação, leitura, atualização e exclusão de tarefas.

A API é construída usando Python, FastAPI e Pydantic.

## Dependências necessárias

- Python
- FastAPI
- Pydantic

Para instalar as dependências, execute o seguinte comando:

```shell
pip install fastapi uvicorn[standard] pydantic
```

## Models

### Task

O modelo `Task` é um objeto Pydantic que representa uma tarefa.

- `id` (int): O identificador único da tarefa.
- `title` (str): O título da tarefa.
- `description` (str): Uma descrição detalhada da tarefa.
- `done` (bool): Um indicador de se a tarefa foi concluída.

## Endpoints

### POST /task/

Cria uma nova tarefa.

- Parâmetros: `task` (Task) - A tarefa a ser criada.

Exemplo de uso:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "title": "New Task", "description": "This is a new task", "done": false}' http://localhost:8000/task/
```

### GET /task/

Retorna uma lista de todas as tareas.

Exemplo de uso:

```shell
curl -X GET http://localhost:8000/task/
```

### GET /task/{task_id}

Retorna uma tarefa por ID.

- Parâmetros: `task_id` (int) - O ID da tarefa a ser recuperada.

Exemplo de uso:

```shell
curl -X GET http://localhost:8000/task/1
```

### PUT /task/{task_id}

Atualiza uma tarefa por ID.

- Parâmetros: 
  - `task_id` (int) - O ID da tarefa a ser atualizada.
  - `task` (Task) - A tarefa atualizada.

Exemplo de uso:

```shell
curl -X PUT -H "Content-Type: application/json" -d '{"id": 1, "title": "Updated Task", "description": "This is an updated task", "done": true}' http://localhost:8000/task/1
```

### DELETE /task/{task_id}

Exclui uma tarefa por ID.

- Parâmetros: `task_id` (int) - O ID da tarefa a ser excluída.

Exemplo de uso:

```shell
curl -X DELETE http://localhost:8000/task/1
```

## Notas importantes

- Se uma tarefa solicitada não existir, a API retornará um erro 404 com a mensagem "Task not found".
- Ao criar ou atualizar tarefas, certifique-se de que o ID da tarefa seja único. A API não verifica automaticamente a unicidade dos IDs. Se você criar duas tarefas com o mesmo ID, apenas a mais recente será preservada.
- As tarefas são armazenadas apenas na memória e serão perdidas quando a aplicação for reiniciada. Para um armazenamento persistente, considere usar um banco de dados.