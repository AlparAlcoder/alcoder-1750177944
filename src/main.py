from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    done: bool


tasks = []

@app.post("/task/", response_model=Task)
def create_task(task: Task):
    """Creates a new task"""
    tasks.append(task.dict())
    return task

@app.get("/task/", response_model=List[Task])
def read_tasks():
    """Returns a list of all tasks"""
    return tasks

@app.get("/task/{task_id}", response_model=Task)
def read_task(task_id: int):
    """Returns a task by id"""
    for task in tasks:
        if task['id'] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/task/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    """Updates a task by id"""
    for index, stored_task in enumerate(tasks):
        if stored_task['id'] == task_id:
            tasks[index] = task.dict()
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    """Deletes a task by id"""
    for index, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(index)
            return {"detail": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")