from pydantic import BaseModel
from pydantic import EmailStr

# Esquema para la solicitud de registro
class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

# Esquema para la respuesta de registro
class RegisterResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

# Esquema para la solicitud de inicio de sesión
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Esquema para la respuesta de inicio de sesión
class LoginResponse(BaseModel):
    access_token: str
    token_type: str