from sqlmodel import Field, SQLModel, create_engine

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    status: bool = False