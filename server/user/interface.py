from mypy_extensions import TypedDict


class UserInterface(TypedDict, total=False):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_no: str
