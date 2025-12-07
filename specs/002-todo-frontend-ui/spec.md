# Phase II Frontend (Todo UI)

## Goal

To provide a modern, interactive user interface (UI) for managing Todo tasks, fully integrated with the existing backend API.

## In Scope

- Creation of a Next.js application structure in the `frontend/` directory.
- Implementation of a data service layer for communication with the Todo API at `http://127.0.0.1:8001`.
- User interface components for viewing, adding, deleting, and toggling the completion status of tasks.
- Responsive layout using Tailwind CSS.

## Out of Scope

- Full user authentication or authorization.
- Advanced task features (e.g., due dates, categories, filtering beyond completion status).
- Complex state management libraries (e.g., Redux, Zustand).
- Deployment configuration (other than initial scaffolding).

## Assumptions

- The backend API is running and accessible at `http://127.0.0.1:8001`.
- The API contract (models and endpoints) defined in the backend feature remains stable.
- The user is using a modern web browser.

## User Scenarios & Testing

### User Story 1 - Task Management Core (Priority: P1)

The user needs to be able to see their tasks, add new ones, mark them as done, and delete them permanently.

**Why this priority**: This covers the core value proposition of a Todo application and is essential for an MVP.

**Independent Test**: Can be fully tested by creating a task, marking it complete, and deleting it, demonstrating full CRUD functionality via the UI.

**Acceptance Scenarios**:

1. **Given** the system has tasks, **When** the user navigates to the homepage, **Then** all existing tasks are displayed with their title and completion status.
2. **Given** the user is on the homepage, **When** they submit the form with a valid task title, **Then** a new task appears in the list, and a creation request is sent to the API.
3. **Given** an incomplete task is visible, **When** the user clicks the completion checkbox, **Then** the task's status is toggled, and an update request is sent to the API.
4. **Given** a task is visible, **When** the user clicks the delete button next to it, **Then** the task is removed from the list, and a deletion request is sent to the API.

### Edge Cases

- **Error Handling**: When an API call (GET, POST, PUT, DELETE) fails, the user must receive a non-disruptive, informative error message on the screen.
- **Empty State**: When no tasks exist in the database, the UI must display a friendly message encouraging the user to add a new task.

## Requirements

### Functional Requirements

- **FR-001**: The system MUST display a list of all Todo tasks.
- **FR-002**: The system MUST provide an input form for adding new tasks (title required, description optional).
- **FR-003**: The system MUST allow users to toggle the completion status of a task.
- **FR-004**: The system MUST allow users to permanently delete a task.
- **FR-005**: The system MUST use a separate service layer (`src/services/api.ts`) to manage all API interactions.

### Key Entities

- **Task**: Represents a single Todo item. Attributes include `id` (integer), `title` (string), `description` (string, optional), and `status` (boolean - true if completed).

## Non-Functional Requirements (NFRs)

- **Performance:** The task list must load and update within 2 seconds on an average network connection.
- **Reliability:** API calls must handle and display errors gracefully without crashing the UI.
- **Usability:** The UI must be responsive and usable on standard desktop and mobile screen sizes.

## Success Criteria (Measurable Outcomes)

- **SC-001**: Users can successfully complete the four core actions (View, Add, Mark Complete, Delete) for a task in under 1 minute.
- **SC-002**: The application successfully connects to the backend API at `http://127.0.0.1:8001` and displays data without requiring manual configuration changes from the end-user.
- **SC-003**: The UI maintains a consistent, responsive, and modern look across different viewport sizes.