from ..base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime

class ModelRole(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    active = Column(String(255))
    date_added = Column(DateTime, default=datetime.now())