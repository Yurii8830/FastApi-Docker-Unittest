from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    name: str
    email: str
    age: int
    active: bool = True
    registration_date: date

class UserDTO(User):
    is_active: bool