from ..base import Base
from .model_role import ModelRole
from .model_user import ModelUser
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime


class ModelUserInRole(Base):
    __tablename__ = 'user_in_role'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))
    date_added = Column(DateTime, default=datetime.now())
    user = relationship(
        ModelUser,
        backref=backref('user',
                        uselist=True))
    role = relationship(
        ModelRole,
        backref=backref('roles',
                        uselist=True))
