from graphene_sqlalchemy import SQLAlchemyObjectType
from database.models.model_role import ModelRole
import graphene


# Create a generic class to mutualize description of role attributes for both queries and mutations
class RoleAttribute:
    name = graphene.String(description="Name of the role.")
    active = graphene.String(description="Active status of the role.")
    date_added = graphene.String(description="Date added of the role.")
   


class Role(SQLAlchemyObjectType, RoleAttribute):
    """Role node."""

    class Meta:
        model = ModelRole
        interfaces = (graphene.relay.Node,)
