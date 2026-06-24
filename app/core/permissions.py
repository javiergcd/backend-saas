from fastapi import Depends, HTTPException

from app.core.security import get_current_user

from app.models.user import User
from app.models.enums import UserRole

def require_admin(
        current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=403,
            detail="Acceso denegado"
        )
    return current_user