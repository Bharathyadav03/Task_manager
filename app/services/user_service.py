# core user logic
# talks to db 
# creates 
# get 
# update




from sqlalchemy.orm import Session
from app.db import models
from app.core.security import hash_password

def create_user(db: Session, user):
    hashed_pwd = hash_password(user.password)
    db_user = models.User(name=user.name, email=user.email, password=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(models.User).all()

def update_user(db: Session, user_id: int, name: str):
    user = get_user(db, user_id)
    if user:
        user.name = name
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
