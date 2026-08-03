from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
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

    existing_user = crud.get_user_by_email(
        db,
        new_user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return crud.create_user(db, new_user)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = crud.get_user_by_email(
        db,
        form_data.username
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        form_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }