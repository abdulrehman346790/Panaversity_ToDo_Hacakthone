# Backend Guidelines - Phase II

## Tech Stack
- **Framework:** FastAPI
- **Database:** SQLModel (PostgreSQL via Neon)
- **Auth:** Better Auth (JWT)
- **Package Manager:** uv (standard python)

## Project Structure
- `main.py`: Application entry point
- `models.py`: Database tables (SQLModel classes)
- `database.py`: Session management
- `routes/`: API endpoints

## Governance
- Always use `core-crud-skill` (SQL variants) for logic.
- All endpoints must be typed with Pydantic/SQLModel.