from contextlib import asynccontextmanager

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi import HTTPException

from src.core.logger import db_logger
from src.core.settings import config

engine = create_async_engine(config.postgres_settings.postgres_async_url)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


async def get_session() -> AsyncSession:
    session = Session()
    try:
        yield session
    except Exception as e:
        db_logger.error(e)
        if isinstance(e, HTTPException):
            raise HTTPException(detail=e.detail, status_code=400)
    finally:
        await session.close()


@asynccontextmanager
async def context_session() -> AsyncSession:
    session = Session()
    try:
        yield session
    except Exception as e:
        db_logger.error(e)
        if isinstance(e, HTTPException):
            raise HTTPException(detail=e.detail, status_code=400)
    finally:
        await session.close()
