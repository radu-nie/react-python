from sqlalchemy import Integer, Column, String
from main import db  # noqa
from .interface import UserInterface


class User(db.Model):  # type: ignore
    """A User Model"""

    __tablename__ = "user"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    phone_no = Column(String(20))

    def update(self, changes: UserInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
