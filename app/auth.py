from passlib.context import CryptContext

from jose import jwt,JWTError
from datetime import datetime, timedelta

SECRET_KEY="mysecretkey"
ALGORITHM="HS256"

def create_access_token(data: dict):

    to_encode=data.copy()

    expire=datetime.utcnow() + timedelta(minutes=30)

    to_encode.update(
        {
            "exp":expire
        }
    )

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token




pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    password = password[:72]
    return pwd_context.hash(password)


def verify_password(
        plain_password:str, 
        hashed_password: str
    ):
    
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_email = payload.get("sub")

        if user_email is None:
            return None

        return user_email

    except JWTError:
        return None