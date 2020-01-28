from graphene_sqlalchemy import SQLAlchemyObjectType
from database.models.model_user_in_role import ModelUserInRole
import graphene


# Create a generic class to mutualize description of user in role attributes for both queries and mutations
class UserInRoleAttribute:
    user_id = graphene.ID(description="ID of the user.")
    role_id = graphene.ID(description="ID of the role.")
    date_added = graphene.String(description="Date added of the user in role.")


class UserInRole(SQLAlchemyObjectType, UserInRoleAttribute):
    """User in role node."""

    class Meta:
        model = ModelUserInRole
        interfaces = (graphene.relay.Node,)
