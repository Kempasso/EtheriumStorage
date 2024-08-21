from typing import Union

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.postgresql.session import Base
from src.core.logger import db_logger


class BaseMixin:
    model: Base
    session: AsyncSession


class RetrieveMixin(BaseMixin):
    async def get_many_by_values(self, offset: Union[int, None] = None, limit: Union[int, None] = None, **kwargs):
        query = select(self.model).filter_by(**kwargs)
        if offset and offset:
            offset = (offset - 1) * limit
            query = query.offset(offset).limit(limit)
        res = await self.session.execute(query)
        return res.scalars().all()

    async def get_first_by_values(self, **kwargs):
        query = select(self.model).filter_by(**kwargs)
        res = await self.session.execute(query)
        return res.scalars().first()


class CreateMixin(BaseMixin):

    async def create(self, **kwargs):
        try:
            prepared_instance = self.model(**kwargs)
            self.session.add(prepared_instance)
            await self.session.commit()
            return prepared_instance
        except Exception as e:
            await self.session.rollback()
            db_logger.error(f"{e}\n"
                            f"Problem throughout create instance of {self.model.__tablename__}")
            raise HTTPException(status_code=400,
                                detail=f"Problem throughout create instance of {self.model.__tablename__}")
