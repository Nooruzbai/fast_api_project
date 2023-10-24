from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from source.config import POSTGRES_DB_USER_NAME, POSTGRES_DB_PASSWORD, POSTGRES_DB_HOST_NAME, POSTGRES_DB_PORT, \
    POSTGRES_DB_NAME

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_DB_USER_NAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST_NAME}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}"


Base = declarative_base()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

