# validates credentials
# generates tokens



from sqlalchemy.orm import Session
from app.db import models
from app.core.security import verify_password, create_access_token

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def login_user(user):
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
