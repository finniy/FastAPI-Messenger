from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.auth_service import AuthService
from app.database.session import get_db
from app.schemas.auth_schemas import UserRegister, UserResponse

router = APIRouter()
auth = AuthService()


@router.post('/register', response_model=UserResponse, status_code=201)
async def register(user_data: UserRegister, db: Session = Depends(get_db)) -> UserResponse:
    user = auth.register(db=db, data=user_data)
    return user
