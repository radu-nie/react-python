from graphene_sqlalchemy import SQLAlchemyObjectType
from database.models.model_user import ModelUser
from datetime import datetime
from database.base import db_session
import graphene
import utils

# Create a generic class to mutualize description of user attributes for both queries and mutations
class UserAttribute:
    first_name = graphene.String(description="First Name of the user.")
    last_name = graphene.String(description="Last name of the user.")
    email = graphene.String(description="Email of the user.")
    phone_no = graphene.String(description="Phone number of the user.")

class User(SQLAlchemyObjectType, UserAttribute):
    """User node."""

    class Meta:
        model = ModelUser
        interfaces = (graphene.relay.Node,)

class CreateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to create a user."""
    pass


class CreateUser(graphene.Mutation):
    """Mutation to create a user."""
    user = graphene.Field(lambda: User, description="User created by this mutation.")

    class Arguments:
        input = CreateUserInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['date_added'] = datetime.utcnow()
        data['date_edited'] = datetime.utcnow()

        user = ModelUser(**data)
        db_session.add(user)
        db_session.commit()

        return CreateUser(user=user)


class UpdateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to update a user."""
    id = graphene.ID(required=True, description="Global Id of the user.")


class UpdateUser(graphene.Mutation):
    """Update a user."""
    user = graphene.Field(lambda: User, description="User updated by this mutation.")

    class Arguments:
        input = UpdateUserInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['date_edited'] = datetime.utcnow()

        user = db_session.query(ModelUser).filter_by(id=data['id'])
        user.update(data)
        db_session.commit()
        user = db_session.query(ModelUser).filter_by(id=data['id']).first()

        return UpdateUser(user=user)