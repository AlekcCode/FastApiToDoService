from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post('/tasks')
async def add_tasks(task: Annotated[STaskAdd, Depends()],):
    tasks.append(task)
    return {'status': True}
