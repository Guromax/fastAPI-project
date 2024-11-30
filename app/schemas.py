from pydantic import BaseModel

class STaskAdd(BaseModel):
    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int

    class Config:
        from_attributes = True

class STaskId(BaseModel):
    ok: bool=True
    task_id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int
