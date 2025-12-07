from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, SQLModel, Field
from typing import List, Optional, Any
from pydantic import BaseModel

# NEW (Correct)
from models import Task
from database import create_db_and_tables, get_session
from core_crud_skill_wrapper import (
    add_task_db,
    get_tasks_db,
    update_task_db,
    delete_task_db
)

# AI / Agents
from agents import Runner, SQLiteSession
from agent import todo_assistant, run_config
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8080", "http://localhost:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    # Ensure tables are created on startup
    create_db_and_tables()

# --- Tasks API ---

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
    tasks = get_tasks_db(session, user_id=None)
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_endpoint(task_id: int, task: Task, session: Session = Depends(get_session)):
    """
    Update an existing task.
    """
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
    return

# --- Chat API ---

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    response: str
    session_id: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chat with the AI Todo Assistant.
    """
    # Create a session instance for this request context
    # SQLiteSession automatically manages persistence based on the session_id and db_path
    session = SQLiteSession(request.session_id, "agent_sessions.db")
    
    try:
        # Run the agent asynchronously using Runner.run
        result = await Runner.run(todo_assistant, request.message, session=session, run_config=run_config)
        # Return the final output string
        return ChatResponse(response=str(result.final_output), session_id=request.session_id)
    except Exception as e:
        import traceback
        traceback.print_exc()
        # Return error as a chat message instead of 500 crash
        error_msg = f"System Error: {str(e)}"
        if "429" in str(e):
            error_msg = "Rate Limit Exceeded. You have used up your free quota for this model. Please try again later or switch models."
        return ChatResponse(response=error_msg, session_id=request.session_id)