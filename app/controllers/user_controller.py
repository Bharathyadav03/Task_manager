# handles request logic between router & service layers
# receives req 
# handles req via pydantic
# fetch data from db
# sends respose

from fastapi import HTTPException
from app.services import user_service

def create_user_controller(db, user):
    return user_service.create_user(db, user)

def get_user_controller(db, user_id):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_all_users_controller(db):
    return user_service.get_all_users(db)

def update_user_controller(db, user_id, name):
    user = user_service.update_user(db, user_id, name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user_controller(db, user_id):
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
