from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Header
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.user import User

from app.schemas.auth import RegisterRequest, RegisterResponse, LoginResponse

from app.core.security import get_password_hash

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# Register a new user
@router.post("/register", response_model=RegisterResponse)
def register(user: RegisterRequest, db: Session  = Depends(get_db)):
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="El correo electrónico ya está registrado"
        )
    new_user = User(
        name=user.name,
        email=user.email,
        password=get_password_hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

from app.core.security import verify_password, create_access_token

@router.post("/login", response_model=LoginResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.email == form_data.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Credenciales de inicio de sesión inválidas"
        )
    
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Credenciales de inicio de sesión inválidas"
        )
    
    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

from app.core.security import get_current_user

@router.get("/me")
def me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }
