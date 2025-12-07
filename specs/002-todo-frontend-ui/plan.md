# Architectural Implementation Plan: Phase II Frontend (Todo UI)

**Feature Branch**: `002-todo-frontend-ui`
**Spec File**: [./spec.md](./spec.md)
**Plan Created**: 2025-12-06
**Status**: Draft

## 1. Scope and Dependencies

### In Scope
- Scaffolding a Next.js application in the `frontend/` directory using the App Router.
- Creating the `src/services/api.ts` service layer for all backend interactions.
- Implementing the `TaskForm.tsx` (task creation) and `TaskList.tsx` (task display/modification) components.
- Integrating components into `src/app/page.tsx` to form the full UI.
- Styling the application using Tailwind CSS for a clean, responsive design.

### Out of Scope
- Global state management (e.g., Redux, Zustand). Simple React state/context will be used.
- Full API authentication/authorization headers.
- Advanced features like filtering, sorting, or complex form validation.

### Technical Dependencies
| Component | Technology | Rationale |
|---|---|---|
| Framework | Next.js 16 (App Router) | User requirement. Provides powerful routing and server components. |
| Styling | Tailwind CSS | User requirement. Utility-first CSS for fast, responsive styling. |
| HTTP Client | Axios | User requirement. Robust client for API service layer. |
| Icons | `react-icons` | User requirement for professional UI elements (checkmarks, trash). |

## 2. Key Decisions and Rationale

| Decision | Rationale | Alternatives Considered | ADR Suggestion |
|---|---|---|---|
| **Architecture** | Use Next.js App Router with an emphasis on **Server Components** for initial data fetching (GET /tasks/) in `page.tsx` to maximize performance and minimize client-side bundles. **Client Components** will be used for interactive elements (`TaskForm.tsx`, `TaskList.tsx` containing client-side state/actions). | Using only Client Components (e.g., using `useState` in `page.tsx` and fetching data in `useEffect`) would increase client bundle size and initial load time. | Yes |
| **Data Flow** | The main page (`page.tsx`) will fetch the initial task list (Server Component). It will then pass the initial list and mutation functions (Add, Delete, Toggle) to the client components. After any client-side mutation, the state will be updated locally and/or the data will be re-fetched (e.g., using `router.refresh()` or a global state refresh mechanism if implemented later). | Using a dedicated context/global store (e.g., Redux) for tasks. Rejected due to the minimal scope (Out of Scope in spec). | No |
| **API Abstraction** | All API calls are strictly encapsulated in `frontend/src/services/api.ts` to enforce separation of concerns (FR5). This file will define type-safe functions for each CRUD operation. | Inline API calls in components (violates FR5 and maintainability). | No |

## 3. Interfaces and API Contracts

### Data Model (`frontend/src/types/task.ts`)
A shared TypeScript interface will be defined to represent the Todo task structure, ensuring type safety across the frontend.

\`\`\`typescript
export interface Task {
    id: number;
    title: string;
    description?: string;
    status: boolean; // true if completed
}

export type TaskCreate = Omit<Task, 'id' | 'status'> & { status?: boolean };
export type TaskUpdate = Partial<TaskCreate>;
\`\`\`

### API Contract (`frontend/src/services/api.ts`)
The base URL is `http://127.0.0.1:8001` (SC-002). Functions will be:

| Function | Method | Endpoint | Description |
|---|---|---|---|
| `getTasks()` | GET | `/tasks/` | Fetch all tasks. Returns `Task[]`. |
| `createTask(data)` | POST | `/tasks/` | Create a new task. Takes `TaskCreate`, returns `Task`. |
| `updateTask(id, data)` | PUT | `/tasks/{id}` | Update an existing task. Takes `id` and `TaskUpdate`, returns `Task`. |
| `deleteTask(id)` | DELETE | `/tasks/{id}` | Delete a task. Takes `id`, returns boolean success. |
| `toggleTask(id)` | PUT | `/tasks/{id}` | Toggles status. Internally calls `updateTask`. |

## 4. Non-Functional Requirements (NFRs) and Budgets

- **Performance (SC-001, NFR):** Leverage Next.js Server Components for fast initial load. All subsequent updates (Add/Toggle/Delete) will use optimistic UI updates where appropriate to meet the <2 second update requirement.
- **Reliability (NFR):** Implement `try...catch` blocks and basic error state handling in all `api.ts` functions and display an error banner or toast notification to the user upon failure (Edge Case: Error Handling).
- **Security:** Use environment variables for the API base URL if deploying, but default to `http://127.0.0.1:8001` as required. No sensitive data will be handled.
- **Cost:** Minimal. Standard hosting for a static Next.js application.

## 5. Data Management and Migration

- **Source of Truth:** Backend API database.
- **Frontend State:** Task list state will be managed in a React Client Component or Context. Component will manage local loading/error states (e.g., button disabled during POST).

## 6. Operational Readiness

- **Observability:** `console.error` and `console.warn` logging for API failures.
- **Deployment:** Standard Next.js build/deploy process (`npm run build`).

## 7. Risk Analysis and Mitigation

| Risk | Blast Radius | Mitigation |
|---|---|---|
| **Scaffolding Failure** | Inability to start the frontend feature. | Manually delete the empty `frontend/` directory and re-run `npx create-next-app@latest frontend/ --typescript --tailwind --eslint` with interactive options if needed. |
| **CORS Issues** | Frontend cannot communicate with the backend API. | Verify backend (FastAPI) has CORS middleware configured to allow `http://localhost:3000` (default Next.js dev port) and the default dev port of the frontend if different. |
| **State Sync Errors** | Task list gets out of sync with the backend after mutations. | Implement a mandatory full re-fetch of the task list after any successful mutation (POST, PUT, DELETE) until a more advanced state management/caching strategy (like SWR/React Query) is introduced. |

## 8. Evaluation and Validation

**Definition of Done (DoD):**
1.  All acceptance scenarios in `spec.md` pass.
2.  All five API CRUD methods are implemented and tested in isolation.
3.  The UI is responsive and passes NFRs (loads under 2 seconds).
4.  All implementation files (scaffold, service, components, page) are created in the `frontend/` directory.

## 9. Architectural Decision Record (ADR)

The selection of the Next.js App Router over the Pages Router for this application, particularly the use of Server Components for initial data fetching, is a significant architectural decision affecting performance, bundling, and future scaling.

📋 Architectural decision detected: **Choosing Next.js App Router and Server Components** — Document reasoning and tradeoffs? Run `/sp.adr nextjs-app-router-selection`