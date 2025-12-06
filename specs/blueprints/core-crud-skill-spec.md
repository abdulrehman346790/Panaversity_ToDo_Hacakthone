# Blueprint: Core CRUD Agent Skill

## Purpose
To create a reusable Claude Code Agent Skill that standardizes the implementation of basic data operations (Create, Read, Update, Delete) across all project phases.

## Required Artifacts
The agent must generate the following structure in `.claude/skills/core-crud-skill/`:

1. **SKILL.md**: A manifest file defining the skill name "core-crud-skill" and its purpose.
2. **CRUD_PATTERN.py**: A Python template file containing these exact stateless function signatures:
   - `add_task(data_store, title, description)`
   - `get_tasks(data_store, status_filter)`
   - `update_task(data_store, task_id, title, description)`
   - `delete_task(data_store, task_id)`
   - `toggle_complete(data_store, task_id)`

## Constraints
- Do NOT implement the actual app logic yet.
- Only generate the skill definition and the python pattern template.