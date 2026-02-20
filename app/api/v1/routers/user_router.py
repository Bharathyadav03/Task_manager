# it handles user related endpoints

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse
from app.controllers import user_controller
from app.api.dependencies import get_db, get_current_user
from app.db import models

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/all_users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return user_controller.create_user_controller(db, user)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return user_controller.get_user_controller(db, user_id)


@router.get("/", response_model=list[UserResponse])
def get_all_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return user_controller.get_all_users_controller(db, skip, limit)


@router.put("/{user_id}")
def update_user(
    user_id: int,
    name: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return user_controller.update_user_controller(db, user_id, name)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return user_controller.delete_user_controller(db, user_id)
