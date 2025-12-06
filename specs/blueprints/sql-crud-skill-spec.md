# Blueprint: SQL CRUD Agent Skill
## Purpose
Evolve `core-crud-skill` to support SQLModel.
## Requirement
Update `.claude/skills/core-crud-skill/CRUD_PATTERN.py` to include:
- `add_task_db(session: Session, task: Task)`
- `get_tasks_db(session: Session, user_id: str)`
- `update_task_db(session: Session, task_id: int, task_data: dict)`