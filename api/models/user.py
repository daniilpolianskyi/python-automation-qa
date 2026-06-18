from pydantic import BaseModel


class LoginUser(BaseModel):
    email: str
    password: str


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
