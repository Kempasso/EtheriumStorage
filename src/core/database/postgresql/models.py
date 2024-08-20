from src.core.database.postgresql.session import Base
from sqlalchemy import Column, DateTime, Integer
from datetime import datetime, timezone


class AbstractBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(tz=timezone.utc),
                        onupdate=datetime.now(tz=timezone.utc))
