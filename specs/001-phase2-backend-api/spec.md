# Feature Specification: Phase II Backend API (Task CRUD)

**Feature Branch**: `001-phase2-backend-api`
**Created**: 2025-12-06
**Status**: Draft
**Input**: User description: "Feature: Phase II Backend API (Task CRUD)

## Goal
Implement a RESTful API using FastAPI and SQLModel that manages Todo tasks in a PostgreSQL database (Neon).

## Technical Requirements
1.  **Location:** All code must be in the `backend/` directory.
2.  **Database:** Use SQLModel to define a `Task` model (table=True) in `backend/models.py`.
3.  **Connection:** Setup the database engine in `backend/database.py` using a `DATABASE_URL` environment variable.
4.  **Reusable Intelligence:** The API logic must strictly use the `_db` functions from `core-crud-skill` (e.g., `add_task_db`).
5.  **API Routes:** Implement the following endpoints in `backend/main.py`:
    * `POST /tasks/`: Create a task.
    * `GET /tasks/`: Read all tasks.
    * `PUT /tasks/{task_id}`: Update a task.
    * `DELETE /tasks/{task_id}`: Delete a task."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create a task (Priority: P1)

An API client wants to create a new task in the system.

**Why this priority**: This is the core functionality to create new tasks.

**Independent Test**: The API client can create a task, and it is stored in the database with the correct title and description.

**Acceptance Scenarios**:

1.  **Given** the API is running, **When** the client sends a POST request to `/tasks/` with a valid JSON payload containing title and description, **Then** a new task is created in the database and the API returns a 201 Created status code with the task details in the response body.
2.  **Given** the API is running, **When** the client sends a POST request to `/tasks/` with an invalid JSON payload (e.g., missing title), **Then** the API returns a 422 Unprocessable Entity status code with an error message.

---

### User Story 2 - Read all tasks (Priority: P1)

An API client wants to retrieve a list of all tasks from the system.

**Why this priority**: This is the main way to see existing tasks.

**Independent Test**: The API client can retrieve a list of tasks with the correct information displayed for each.

**Acceptance Scenarios**:

1.  **Given** there are tasks in the database, **When** the client sends a GET request to `/tasks/`, **Then** the API returns a 200 OK status code with a JSON array containing all tasks in the response body.
2.  **Given** there are no tasks in the database, **When** the client sends a GET request to `/tasks/`, **Then** the API returns a 200 OK status code with an empty JSON array in the response body.

---

### User Story 3 - Update a task (Priority: P2)

An API client wants to update the title and/or description of an existing task.

**Why this priority**: Allows modification of existing tasks.

**Independent Test**: The API client can update a task, and the changes are reflected in the database.

**Acceptance Scenarios**:

1.  **Given** the API is running and a task exists, **When** the client sends a PUT request to `/tasks/{task_id}` with a valid JSON payload containing the updated title and/or description, **Then** the task is updated in the database and the API returns a 200 OK status code with the updated task details in the response body.
2.  **Given** the API is running and a task exists, **When** the client sends a PUT request to `/tasks/{task_id}` with an invalid task ID, **Then** the API returns a 404 Not Found status code.

---

### User Story 4 - Delete a task (Priority: P2)

An API client wants to delete a task from the system.

**Why this priority**: Allows removal of tasks.

**Independent Test**: The API client can delete a task, and it is removed from the database.

**Acceptance Scenarios**:

1.  **Given** the API is running and a task exists, **When** the client sends a DELETE request to `/tasks/{task_id}`, **Then** the task is removed from the database and the API returns a 204 No Content status code.
2.  **Given** the API is running and a task exists, **When** the client sends a DELETE request to `/tasks/{task_id}` with an invalid task ID, **Then** the API returns a 404 Not Found status code.

---

## Edge Cases

-   What happens when the database connection fails? (The API should return a 500 Internal Server Error with an appropriate error message)
-   How does the API handle concurrent requests? (This should be handled by the database and SQLModel.)
-   What happens when the user tries to create a task with an empty title? (The API should return a 422 Unprocessable Entity error.)

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: System MUST allow API clients to create tasks with a title and description.
-   **FR-002**: System MUST allow API clients to view a list of all tasks, including their ID, title, and description.
-   **FR-003**: System MUST allow API clients to update the title and description of a task.
-   **FR-004**: System MUST allow API clients to delete a task.
-   **FR-005**: The API logic MUST strictly use the `_db` functions from `core-crud-skill`.
-   **FR-006**: The database MUST be a PostgreSQL database managed by Neon.
-   **FR-007**: The database engine MUST be set up using a `DATABASE_URL` environment variable.
-   **FR-008**: All code MUST be in the `backend/` directory.
-   **FR-009**: Use SQLModel to define a `Task` model (table=True) in `backend/models.py`.
-   **FR-010**: Implement the following endpoints in `backend/main.py`:
    * `POST /tasks/`: Create a task.
    * `GET /tasks/`: Read all tasks.
    * `PUT /tasks/{task_id}`: Update a task.
    * `DELETE /tasks/{task_id}`: Delete a task.

### Key Entities *(include if feature involves data)*

-   **Task**: Represents a task in the todo list.
    Attributes: ID (unique identifier), Title (task name), Description (task details).

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: API clients can successfully create, read, update, and delete tasks via the API endpoints.
-   **SC-002**: The API endpoints adhere to RESTful principles and use appropriate HTTP status codes.
-   **SC-003**: The application uses SQLModel to interact with the PostgreSQL database.
