from pydantic import BaseModel

from database import new_session, TaskOrm
from Schema import STaskAdd, STask, STaskId
from sqlalchemy import select


class RepositoryTask:
    @classmethod
    async def add_data(cls, task: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = task.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def get_data(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schema = [STask(**{
                'id': task_model.id,
                'name': task_model.name,
                'description': task_model.description
            }) for task_model in task_models]
            return task_schema
