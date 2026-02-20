from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.routers import user_router, auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Industry Level FastAPI Project")

app.include_router(user_router.router)
app.include_router(auth_router.router)
