# Blueprint: Frontend Service Agent Skill

## Purpose
To standardize how the Next.js frontend communicates with the FastAPI backend, ensuring type safety and cleaner UI components.

## Required Artifacts
The agent must generate `.claude/skills/frontend-service-skill/` containing:

1. **SKILL.md**: Instructions to always separate API calls from UI components.
2. **API_PATTERN.ts**: A TypeScript template for the API client:
   - `fetchTasks()`
   - `createTask(title: string, description?: string)`
   - `updateTask(id: number, updates: any)`
   - `deleteTask(id: number)`
   - Must use a configured `axios` or `fetch` instance with Base URL.