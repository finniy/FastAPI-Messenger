from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.cruds.user_crud import UserCRUD
from app.utils.password import verify_password, hash_password
from app.schemas.auth_schemas import UserRegister
from app.models.auth_model import User


class AuthService:
    def __init__(self):
        self.user_crud = UserCRUD()

    def register(self, db: Session, data: UserRegister) -> User:

        # Проверка nickname
        if self.user_crud.read_by_nickname(db, data.nickname):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Nickname already taken"
            )

        # Проверка email
        if self.user_crud.read_by_email(db, data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Хеширование пароля
        password_hash = hash_password(data.password)

        # Создание пользователя
        return self.user_crud.create(
            db=db,
            username=data.username,
            nickname=data.nickname,
            email=data.email,
            password_hash=password_hash
        )


auth_service = AuthService()
