from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    username: str
    nickname: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    nickname: str
    email: EmailStr

    class Config:
        from_attributes = True
