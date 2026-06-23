from pwdlib import PasswordHash

from datetime import datetime, timedelta

from jose import jwt

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.user import User
from app.services.user_service import UserService

password_hash = PasswordHash.recommended()

# Encriptar la contraseña
def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

# Verificar la contraseña
def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(
        password,
        hashed_password
    )

# Crear el token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update(
        {
            "exp": expire
        }
    )
    
    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

# Verificar el token
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
    )

# Obtener el usuario actual
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )
        
        user_id = int(user_id)
    except (JWTError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )
    
    user = UserService.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Usuario no encontrado"
        )
    
    return user