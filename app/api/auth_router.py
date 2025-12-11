from fastapi import APIRouter, Depends, HTTPException, status

from app.database.session import get_db
from app.schemas.auth_schemas import UserRegister, UserResponse

router = APIRouter()


@router.post('/register', response_model=UserResponse)
async def register(user_data: UserRegister, db: Depends(get_db)):
    # вызов сервиса будет
    pass
