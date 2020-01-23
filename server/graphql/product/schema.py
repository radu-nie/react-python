import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from model import db_session, Department as DepartmentModel, Employee as EmployeeModel, User as UserModel, Role as RoleModel, UserInRole as UserInRoleModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class DepartmentConnections(relay.Connection):
    class Meta:
        node = Department


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class EmployeeConnections(relay.Connection):
    class Meta:
        node = Employee


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)


class UserConnections(relay.Connection):
    class Meta:
        node = User


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node,)


class RoleConnections(relay.Connection):
    class Meta:
        node = Role


class UserInRole(SQLAlchemyObjectType):
    class Meta:
        model = UserInRoleModel
        interfaces = (relay.Node, )


class UserInRoleConnections(relay.Connection):
    class Meta:
        node = UserInRole


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(EmployeeConnections)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(
        DepartmentConnections, sort=None,)

    all_users = SQLAlchemyConnectionField(UserConnections)
    all_roles = SQLAlchemyConnectionField(RoleConnections)
    user_in_role = SQLAlchemyConnectionField(UserInRoleConnections)


class Mutation(graphene.ObjectType):
    node = relay.Node.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
