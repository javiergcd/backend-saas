from pwdlib import PasswordHash

from datetime import datetime, timedelta

from jose import jwt

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

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