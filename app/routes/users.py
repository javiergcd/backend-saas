from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate

from typing import List

from app.database.dependencies import get_db

router = APIRouter()

# Endpoint para crear un nuevo usuario
@router.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        id=new_user.id,
        name=new_user.name,
        email=new_user.email
    )

# Endpoint para obtener todos los usuarios
@router.get("/users", response_model=List[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    users = db.query(User).all()
    return users

# Endpoint para obtener un usuario por su ID
@router.get("/users/{useri_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Endpoint para eliminar un usuario por su ID
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(user)
    db.commit()

    return{"message": "Usuario eliminado exitosamente"}

# Endpoint para actualizar un usuario por su ID
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404, 
            detail="Usuario no encontrado"
        )
    user.name = user_data.name
    user.email = user_data.email
    db.commit()
    db.refresh(user)

    return user