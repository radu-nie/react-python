from main import db
from typing import List
from .model import User
from .interface import UserInterface
from sqlalchemy import exc
from logging import exception


class UserService:
    @staticmethod
    def get_all() -> List[User]:
        users = User.query.all()
        return users

    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.get(id)

    @staticmethod
    def get_by_email(email: str) -> User:
        user = User.query.filter(User.email == email).first()
        if not user:
            return []
        return user

    @staticmethod
    def update(user: User, User_change_updates: UserInterface) -> User:
        user.update(User_change_updates)
        db.session.commit()
        return user

    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        user = User.query.filter(User.id == id).first()
        if not user:
            return []
        db.session.delete(user)
        db.session.commit()
        return [id]

    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        new_user = User(first_name=new_attrs["first_name"],
                        last_name=new_attrs["last_name"], email=new_attrs["email"], phone_no=new_attrs["phone_no"])

        try:
            db.session.add(new_user)
            db.session.commit()

        except exc.IntegrityError as e:
            db.session.rollback()
            exception("Integrity Error")
        else:
            return new_user

    @staticmethod
    def get_roles_by_id(email: str) -> User:
        user = User.query.filter(User.email == email).first()
        if not user:
            return []
        return user
