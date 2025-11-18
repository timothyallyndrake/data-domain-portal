import datetime
from sqlalchemy import func, JSON, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class RawOrder(Base):
    __tablename__ = "raw_orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
