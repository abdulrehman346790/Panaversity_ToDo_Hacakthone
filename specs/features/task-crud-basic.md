# Feature: Basic Task CRUD (Console App)

## Goal
Implement the core Todo application features where task data is stored in a list of dictionaries in memory.

## Acceptance Criteria using `core-crud-skill`

### 1. Add Task
* **User Action:** Prompt for task title and description.
* **Logic:** Use `add_task()` from the Agent Skill.
* **System Response:** Display confirmation with the new Task ID.

### 2. View Task List
* **User Action:** Select option to view all tasks.
* **Logic:** Use `get_tasks()` from the Agent Skill.
* **System Response:** Display all tasks in a table format (ID | Status | Title).

### 3. Update Task
* **User Action:** Prompt for Task ID, then new title/description.
* **Logic:** Use `update_task()` from the Agent Skill.

### 4. Delete Task
* **User Action:** Prompt for Task ID.
* **Logic:** Use `delete_task()` from the Agent Skill.

### 5. Mark as Complete
* **User Action:** Prompt for Task ID.
* **Logic:** Use `toggle_complete()` from the Agent Skill.

## Application Loop
The app must run in a `while` loop displaying a menu until the user chooses "Exit".