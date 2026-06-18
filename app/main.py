from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base

from app.models.user import User
from app.routes.users import router as users_router

from app.routes.auth import router as auth_router

from app.routes.files import router as files_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)    # Agrega el router de usuarios
app.include_router(auth_router)     # Agrega el router de autenticación

app.include_router(files_router)    # Agrega el router de archivos

@app.get("/")
def home():
    return{
        "message": "Backend SaaS is running!"
    }
