# Feature Tasks: Phase II Frontend (Todo UI)

**Feature Branch**: `002-todo-frontend-ui`
**Spec File**: [./spec.md](./spec.md)
**Plan File**: [./plan.md](./plan.md)
**Tasks Generated**: 2025-12-06
**MVP Scope**: User Story 1 - Task Management Core

## Task Dependencies

This feature is designed for incremental delivery. User Story 1 (US1) is the MVP and can be developed independently of hypothetical future stories. Tasks within US1 must be completed sequentially, although some can be run in parallel where marked [P].

## Phase 1: Setup and Scaffolding

Goal: Initialize the Next.js project and set up core dependencies.

- [ ] T001 Scaffold Next.js application in `frontend/` directory using: `npx create-next-app@latest frontend/ --typescript --tailwind --eslint`
- [ ] T002 Move into `frontend/` and install required packages: `npm install axios react-icons`
- [ ] T003 Configure base URL in `frontend/src/services/api.ts` to `http://127.0.0.1:8001` (Plan, Sec 3, API Contract)

## Phase 2: Foundational Components and Service Layer

Goal: Create shared types and the API service layer (FR5).

- [ ] T004 Create task type definitions in `frontend/src/types/task.ts` (Plan, Sec 3, Data Model)
- [ ] T005 [P] Implement `getTasks()` in `frontend/src/services/api.ts` (GET `/tasks/`)
- [ ] T006 [P] Implement `createTask(data)` in `frontend/src/services/api.ts` (POST `/tasks/`)
- [ ] T007 [P] Implement `updateTask(id, data)` in `frontend/src/services/api.ts` (PUT `/tasks/{id}`)
- [ ] T008 [P] Implement `deleteTask(id)` in `frontend/src/services/api.ts` (DELETE `/tasks/{id}`)
- [ ] T009 [P] Implement `toggleTask(id)` in `frontend/src/services/api.ts` (internally calls `updateTask`)

## Phase 3: User Story 1 - Task Management Core [US1]

Goal: Implement the full UI for CRUD operations (View, Add, Toggle, Delete).
Independent Test: Verify a task can be created, seen, marked complete, and deleted via the UI.

- [ ] T010 [P] [US1] Update `frontend/src/app/layout.tsx` to include Tailwind styling setup if not automatically configured (Scaffold result).
- [ ] T011 [P] [US1] Create the `TaskForm` component in `frontend/src/components/TaskForm.tsx` (FR2, Edge Case: Empty State)
    - Should handle form state, call `createTask`, and report success/error.
- [ ] T012 [P] [US1] Create the `TaskList` component in `frontend/src/components/TaskList.tsx` (FR1, FR3, FR4)
    - Should render a list, handle task deletion and toggling status using the API service.
- [ ] T013 [US1] Integrate `TaskForm` and `TaskList` components into the main `frontend/src/app/page.tsx` (Integration)
    - `page.tsx` should be a Server Component to fetch initial data using `getTasks()`.
    - `page.tsx` should handle the state/refresh logic for task mutations (e.g., using a client component wrapper or `router.refresh()`).
- [ ] T014 [US1] Implement basic error display logic for API failures in a central place (e.g., in a Context or in `page.tsx`) (Edge Case: Error Handling)

## Final Phase: Polish and Validation

- [ ] T015 Validate UI responsiveness and styling using Tailwind CSS (NFRs, SC-003)
- [ ] T016 Final review of all files against the plan and spec.

## Parallel Execution Opportunities

The following tasks can be executed in parallel after Phase 1 and T004 are complete:

- API Service Implementation: T005, T006, T007, T008, T009
- UI Component Development: T010, T011, T012

## Implementation Strategy

The strategy is a Minimal Viable Product (MVP) approach focused on User Story 1. The implementation will be incremental, starting with infrastructure setup (Phase 1), followed by the API service layer (Phase 2), and finally integrating the UI components (Phase 3). Every task will be treated as an atomic change and committed upon completion.
