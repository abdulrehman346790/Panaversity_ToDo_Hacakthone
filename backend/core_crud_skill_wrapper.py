import sys
import os

# 1. Get the path to the current file (backend/core_crud_skill_wrapper.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Calculate the path to the hidden skill folder
#    (Go up one level from 'backend' to root, then into '.claude/skills/core-crud-skill')
skill_path = os.path.join(current_dir, "..", ".claude", "skills", "core-crud-skill")

# 3. Add this path to Python's system path so it can "see" the files
sys.path.append(skill_path)

# 4. Now standard imports will work because Python knows where to look
try:
    from CRUD_PATTERN import (
        add_task_db,
        get_tasks_db,
        update_task_db,
        delete_task_db,
        toggle_complete_db
    )
except ImportError as e:
    print(f"CRITICAL ERROR: Could not import Agent Skill. Checked path: {skill_path}")
    raise e