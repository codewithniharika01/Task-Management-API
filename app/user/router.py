from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app import crud
from app.user.schema import UserCreate, UserLogin, UserResponse

from app.auth import create_access_token, verify_password
router = APIRouter()


@router.post("/register",response_model=UserResponse)

def register(
    new_user: UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, new_user)


@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    user = crud.get_user_by_email(
        db,
        user_data.email
    )

    if not user:
        return {"message": "User not found"}

    if not verify_password(user_data.password, user.password):
        return {"message": "Wrong password"}

    token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }