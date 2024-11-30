from fastapi import APIRouter, Depends
from typing import Annotated
from app.crud import TaskRepository
from app.schemas import STaskAdd, STaskId, STask

router = APIRouter(tags=["Current tasks"])

@router.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
        task_id = await TaskRepository.add_one(task)
        return {"ok": True, "task": task_id}

@router.get("/tasks")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks

