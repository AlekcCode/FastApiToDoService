from Schema import STaskAdd, STask, STaskId
from typing import Annotated, List
from fastapi import Depends
from fastapi import APIRouter

from repository import RepositoryTask

router = APIRouter(
    prefix="/tasks",
    tags=['ToDo']
)


@router.post('', response_model=STaskId)
async def add_tasks(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await RepositoryTask.add_data(task)
    return STaskId(ok=True, task_id=task_id)


@router.get('', response_model=List[STask])
async def get_tasks() -> List[STask]:
    tasks = await RepositoryTask.get_data()
    return tasks