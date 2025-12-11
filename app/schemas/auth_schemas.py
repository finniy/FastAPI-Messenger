from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime


class UserRegister(BaseModel):
    username: str = Field(..., min_length=2, max_length=30)
    nickname: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str):
        if v.isdigit():
            raise ValueError("Пароль не может содержать только цифры")
        if v.isalpha():
            raise ValueError("Пароль не может содержать только буквы")
        return v


class UserResponse(BaseModel):
    id: int
    username: str
    nickname: str
    email: EmailStr
    created_at: datetime

    model_config = {"from_attributes": True}
