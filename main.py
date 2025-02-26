from fastapi import FastAPI
from router import router
from database import create_database, delete_database
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_database()
    print('Очистка')
    await create_database()
    print('БД готова к работе')
    yield
    print('Выключение')
app = FastAPI(lifespan=lifespan)
app.include_router(router)
