import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
# Import OpenAIChatCompletionsModel to wrap the custom client
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
from agents.run import RunConfig
from sqlmodel import Session

# Try/Except block handles imports whether running from root or backend folder
try:
    from backend.core_crud_skill_wrapper import add_task_db, get_tasks_db, update_task_db, delete_task_db
    from backend.database import engine
    from backend.models import Task
except ImportError:
    from core_crud_skill_wrapper import add_task_db, get_tasks_db, update_task_db, delete_task_db
    from database import engine
    from models import Task

# Load environment variables
load_dotenv()

# --- 1. Gemini Client Configuration ---
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env. Please check your backend/.env file.")

# Connect to Google's OpenAI-compatible endpoint
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create the Model object wrapping the client
# Note: Use 'gemini-2.0-flash' or 'gemini-1.5-flash' depending on availability
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", 
    openai_client=client
)

# Helper for Database Session
def get_session():
    return Session(engine)

# --- 2. Tool Definitions (Wrapped Skills) ---

@function_tool
def add_task(title: str, description: str = None) -> str:
    """Adds a new task to the user's todo list."""
    with get_session() as session:
        task = Task(title=title, description=description)
        result = add_task_db(session, task)
        return f"Added task: {result.title} (ID: {result.id})"

@function_tool
def list_tasks() -> str:
    """Lists all tasks in the todo list."""
    with get_session() as session:
        tasks = get_tasks_db(session)
        if not tasks:
            return "No tasks found."
        return "\n".join([f"{t.id}. {t.title} [{'Done' if t.status else 'Pending'}]" for t in tasks])

@function_tool
def update_task(task_id: int, title: str = None, description: str = None, status: bool = None) -> str:
    """Updates an existing task."""
    with get_session() as session:
        updates = {}
        if title is not None: updates['title'] = title
        if description is not None: updates['description'] = description
        if status is not None: updates['status'] = status
        
        result = update_task_db(session, task_id, updates)
        if result:
            return f"Updated task {task_id}: {result.title}"
        return f"Task {task_id} not found."

@function_tool
def delete_task(task_id: int) -> str:
    """Deletes a task by ID."""
    with get_session() as session:
        success = delete_task_db(session, task_id)
        if success:
            return f"Deleted task {task_id}."
        return f"Task {task_id} not found."

# --- 3. Agent Definition ---

todo_assistant = Agent(
    name="TodoAssistant",
    instructions="You are a helpful assistant. You manage the user's todo list. Be concise.",
    model=model,  # Pass the wrapped model object here
    tools=[add_task, list_tasks, update_task, delete_task]
)

# --- 4. Run Configuration ---
run_config = RunConfig(
    tracing_disabled=True
)

if __name__ == "__main__":
    async def main():
        print("🤖 Todo Assistant (Gemini) Ready. Type 'exit' to quit.")
        while True:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            # Run the agent
            result = await Runner.run(todo_assistant, user_input, run_config=run_config)
            print(f"Agent: {result.final_output}")

    asyncio.run(main())