from marshmallow import fields, Schema


class UserSchema(Schema):
    """User schema"""

    id = fields.Number(attribute="id")
    first_name = fields.String(attribute="first_name")
    last_name = fields.String(attribute="last_name")
    email = fields.String(attribute="email")
    phone_no = fields.String(attribute="phone_no")
    many = True
