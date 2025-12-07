from typing import List, Optional, Any, Dict
from sqlmodel import Session, select

# --- Core CRUD functions for SQLModel ---

def add_task_db(session: Session, task: Any) -> Any:
    """Adds a new task to the database."""
    # Logic: Add, Commit, Refresh
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_tasks_db(session: Session, user_id: Optional[str] = None) -> List[Any]:
    """Retrieves tasks from the database."""
    # Import INSIDE to avoid ModuleNotFoundError
    from models import Task 
    
    statement = select(Task)
    # We will add user_id filtering later for Auth
    # if user_id:
    #     statement = statement.where(Task.user_id == user_id)
        
    results = session.exec(statement)
    return results.all()

def update_task_db(session: Session, task_id: int, task_data: Dict[str, Any]) -> Optional[Any]:
    """Updates an existing task by ID."""
    from models import Task
    
    task = session.get(Task, task_id)
    if task:
        # Loop through the dictionary and update fields
        for key, value in task_data.items():
            setattr(task, key, value)

        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    return None

def delete_task_db(session: Session, task_id: int) -> bool:
    """Deletes a task by ID."""
    from models import Task
    
    task = session.get(Task, task_id)
    if task:
        session.delete(task)
        session.commit()
        return True
    return False

def toggle_complete_db(session: Session, task_id: int) -> Optional[Any]:
    """Toggles the completion status of a task by ID."""
    from models import Task
    
    task = session.get(Task, task_id)
    if task:
        task.status = not task.status
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    return None


# --- Legacy / In-Memory Interface (Preserved for compatibility) ---

def add_task(data_store, title, description):
    pass

def get_tasks(data_store, status_filter):
    pass

def update_task(data_store, task_id, title, description):
    pass

def delete_task(data_store, task_id):
    pass

def toggle_complete(data_store, task_id):
    pass