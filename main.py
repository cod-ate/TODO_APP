from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

todos= []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

# POST API
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"TODO added", 
        "data":todo
    }

# GET API
@app.get("/todos")
def get_todos():
    return todos


# this is donr using dynamic routing and path parameters (/todos/todo_id)
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo

    return {
        "error": "todo not found"
        }


# PUT API
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo):
    for i,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i]= updated_todo
            return {
                "message":"Data updated",
                "data": updated_todo
            }
    return {"error":"todo not found"}    


# DELETE API
@app.delete("/todos/{todo_id}")
def deleted_todo(todo_id:int):
    for i,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message":"Data Deleted"}
    return {"error":"data not found"}