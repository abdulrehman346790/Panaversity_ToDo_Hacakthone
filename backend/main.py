from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, SQLModel, Field
from typing import List, Optional

# NEW (Correct)
from models import Task
from database import create_db_and_tables, get_session
from core_crud_skill_wrapper import (
    add_task_db,
    get_tasks_db,
    update_task_db,
    delete_task_db
)
app = FastAPI()

@app.on_event("startup")
def on_startup():
    # Ensure tables are created on startup
    create_db_and_tables()

@app.post("/tasks/", response_model=Task)
def create_task_endpoint(task: Task, session: Session = Depends(get_session)):
    """
    Create a new task.
    """
    db_task = add_task_db(session, task)
    return db_task

@app.get("/tasks/", response_model=List[Task])
def read_tasks_endpoint(session: Session = Depends(get_session)):
    """
    Retrieve all tasks.
    """
    # Assuming get_tasks_db can retrieve all tasks without a specific user_id for now
    tasks = get_tasks_db(session, user_id=None) # Pass None or adjust skill function
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_endpoint(task_id: int, task: Task, session: Session = Depends(get_session)):
    """
    Update an existing task.
    """
    # Create a dictionary of fields to update, excluding id and potentially other defaults
    task_data = task.dict(exclude_unset=True)
    db_task = update_task_db(session, task_id, task_data)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task_endpoint(task_id: int, session: Session = Depends(get_session)):
    """
    Delete a task.
    """
    success = delete_task_db(session, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    # For a 204 No Content response, typically no body is returned.
    # FastAPI handles this automatically if nothing is explicitly returned.
    # Returning an empty dict or None would also work, but just `return` for 204.
    return