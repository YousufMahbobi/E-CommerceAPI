from sqlalchemy.ext.asyncio import (create_async_engine, AsyncAttrs, async_sessionmaker,
                                    AsyncSession)
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings


class Base(AsyncAttrs, DeclarativeBase):
    pass


engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=True,
)

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with async_session() as session:
        yield session