from sqlalchemy.orm import Session
from app.models.auth_model import User


class UserCRUD:
    def create(self, db: Session, username: str, nickname: str, email: str, password_hash: str) -> User:
        user = User(
            username=username,
            nickname=nickname,
            email=email,
            password_hash=password_hash
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def read_by_id(self, db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()

    def read_by_email(self, db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    def read_by_nickname(self, db: Session, nickname: str) -> User | None:
        return db.query(User).filter(User.nickname == nickname).first()

    def update_username(self, db: Session, user_id: int, username: str) -> User | None:
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None

        user.username = username
        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int) -> bool:
        deleted_count = db.query(User).filter(User.id == user_id).delete()

        if deleted_count == 0:
            return False

        db.commit()
        return True
