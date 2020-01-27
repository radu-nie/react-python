from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
# import schema_role
# import schema_user
# import schema_user_in_role
from schemas.schema_role import *
from schemas.schema_user import *
from schemas.schema_user_in_role import *

class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()
    user = graphene.relay.Node.Field(User)
    userList = SQLAlchemyConnectionField(User)
    role = graphene.relay.Node.Field(Role)
    roleList = SQLAlchemyConnectionField(Role)
    userInRole = graphene.relay.Node.Field(UserInRole)
    userInRoleList = SQLAlchemyConnectionField(UserInRole)

class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()
    updateUser = UpdateUser.Field()
    # createPlanet = schema_planet.CreatePlanet.Field()
    # updatePlanet = schema_planet.UpdatePlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)