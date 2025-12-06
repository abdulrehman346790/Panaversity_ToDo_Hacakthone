from sqlmodel import create_engine, Session
import os

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    from models import Task
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session