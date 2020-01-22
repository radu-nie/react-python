from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import UserSchema
from .service import UserService
from .model import User
from .interface import UserInterface

api = Namespace("User", description="User entity")  # noqa


@api.route("/")
class UserResource(Resource):
    """Users"""

    @responds(schema=UserSchema, many=True)
    def get(self) -> List[User]:
        """Get all Users"""

        users = UserService.get_all()
        return users

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def post(self) -> User:
        """Create a Single User"""

        return UserService.create(request.parsed_obj)


@api.route("/<int:userId>")
@api.param("userId", "User ID")
class UserIdResource(Resource):
    @responds(schema=UserSchema)
    def get(self, userId: int) -> User:
        """Get User by Id"""

        return UserService.get_by_id(userId)

    def delete(self, userId: int) -> Response:
        """Delete User by Id"""
        from flask import jsonify

        id = UserService.delete_by_id(userId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=UserSchema, api=api)
    @responds(schema=UserSchema)
    def put(self, userId: int) -> User:
        """Update Single User"""

        changes: UserInterface = request.parsed_obj
        user = UserService.get_by_id(userId)
        return UserService.update(user, changes)


@api.route("/<string:email>")
@api.param("email", "Email")
class UserEmailResource(Resource):
    @responds(schema=UserSchema)
    def get(self, email: str) -> User:
        """Get User by email"""

        return UserService.get_by_email(email)
