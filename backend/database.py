from sqlmodel import create_engine, Session, SQLModel
import os

# 1. Try to get the URL from the environment
# 2. If NOT found, fallback to a local SQLite file named 'todo.db'
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./todo.db")

# 3. Fix for Neon/Postgres URLs (SQLAlchemy requires postgresql://, not postgres://)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 4. Create the engine
# check_same_thread=False is needed only for SQLite
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

def create_db_and_tables():
    # Import models here to ensure they are registered with SQLModel before creation
    from models import Task
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session