from .base import Base
from sqlalchemy import Column, Integer, String, Numeric, Date


class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    kind = Column(String)
    amount = Column(Numeric(8, 2))
    description = Column(String, nullable=True)