from fastapi import FastAPI
from app.routers import tasks
from app.database import Base
from contextlib import asynccontextmanager
from app.database import create_tables
from sqlalchemy.ext.asyncio import AsyncEngine


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("Database is ready for work")
    yield
    print("Switching off...")


# Создаем таблицы, если их нет
async def init_db(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Создаем приложение
app = FastAPI()

# Подключаем роутеры
app.include_router(tasks.router)
