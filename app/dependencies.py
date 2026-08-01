from app.db import SessionLocal
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.auth import verify_token
from app import crud



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    email = verify_token(token)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = crud.get_user_by_email(
        db,
        email
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user