from ..base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime

class ModelUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    phone_no = Column(String(20))
    date_added = Column(DateTime, default=datetime.now())
    date_edited = Column(DateTime, default=datetime.now())
