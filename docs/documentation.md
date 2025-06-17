# Task Management API

## Descri��o geral

Este � um exemplo simples de uma API de gerenciamento de tarefas usando FastAPI. A API permite a cria��o, leitura, atualiza��o e exclus�o de tarefas.

A API � constru�da usando Python, FastAPI e Pydantic.

## Depend�ncias necess�rias

- Python
- FastAPI
- Pydantic

Para instalar as depend�ncias, execute o seguinte comando:

```shell
pip install fastapi uvicorn[standard] pydantic
```

## Models

### Task

O modelo `Task` � um objeto Pydantic que representa uma tarefa.

- `id` (int): O identificador �nico da tarefa.
- `title` (str): O t�tulo da tarefa.
- `description` (str): Uma descri��o detalhada da tarefa.
- `done` (bool): Um indicador de se a tarefa foi conclu�da.

## Endpoints

### POST /task/

Cria uma nova tarefa.

- Par�metros: `task` (Task) - A tarefa a ser criada.

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

- Par�metros: `task_id` (int) - O ID da tarefa a ser recuperada.

Exemplo de uso:

```shell
curl -X GET http://localhost:8000/task/1
```

### PUT /task/{task_id}

Atualiza uma tarefa por ID.

- Par�metros: 
  - `task_id` (int) - O ID da tarefa a ser atualizada.
  - `task` (Task) - A tarefa atualizada.

Exemplo de uso:

```shell
curl -X PUT -H "Content-Type: application/json" -d '{"id": 1, "title": "Updated Task", "description": "This is an updated task", "done": true}' http://localhost:8000/task/1
```

### DELETE /task/{task_id}

Exclui uma tarefa por ID.

- Par�metros: `task_id` (int) - O ID da tarefa a ser exclu�da.

Exemplo de uso:

```shell
curl -X DELETE http://localhost:8000/task/1
```

## Notas importantes

- Se uma tarefa solicitada n�o existir, a API retornar� um erro 404 com a mensagem "Task not found".
- Ao criar ou atualizar tarefas, certifique-se de que o ID da tarefa seja �nico. A API n�o verifica automaticamente a unicidade dos IDs. Se voc� criar duas tarefas com o mesmo ID, apenas a mais recente ser� preservada.
- As tarefas s�o armazenadas apenas na mem�ria e ser�o perdidas quando a aplica��o for reiniciada. Para um armazenamento persistente, considere usar um banco de dados.