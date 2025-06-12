from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email:str


class UserCreate(UserBase):
    pass

class User(UserCreate):
    id: int
    is_active: bool = True