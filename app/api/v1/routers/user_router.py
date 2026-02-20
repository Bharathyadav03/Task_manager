# it handles user related endpoints


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.user_schema import UserCreate, UserResponse
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user_controller(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.get_user_controller(db, user_id)

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_controller.get_all_users_controller(db)

@router.put("/{user_id}")
def update_user(user_id: int, name: str, db: Session = Depends(get_db)):
    return user_controller.update_user_controller(db, user_id, name)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.delete_user_controller(db, user_id)
