from pydantic import BaseModel, ConfigDict

# Esquema para crear un nuevo usuario
class UserCreate(BaseModel):
    name: str
    email: str

# Esquema para la respuesta de un usuario
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True
    )

# Esquema para actualizar un usuario
class UserUpdate(BaseModel):
    name: str
    email: str
