import random
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, HTTPException, status
from jose import jwt

from src.core.redis import redis_client
from src.core.settings import settings
from src.models.auth import EmailSchema, LoginRequest, Token

router = APIRouter()

CODE_EXPIRY_SECONDS = 300  # 5 minutes

@router.post("/request-code", status_code=status.HTTP_200_OK)
def request_access_code(payload: EmailSchema):
    email = payload.email
    code = str(random.randint(100000, 999999))

    print("=" * 50)
    print(f"VERIFICATION CODE for {email}: {code}")
    print("=" * 50)

    redis_client.set(f"auth_code:{email}", code, ex=CODE_EXPIRY_SECONDS)

    return {"message": f"Verification code sent for {email}. Please check the console."}


@router.post("/login", response_model=Token)
def login_with_code(payload: LoginRequest):
    email = payload.email
    code = payload.code

    stored_code = redis_client.get(f"auth_code:{email}")

    if not stored_code:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Verification code has expired or was not requested.",
        )

    if stored_code != code:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The provided verification code is incorrect.",
        )

    redis_client.delete(f"auth_code:{email}")

    expires_delta = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"exp": expire, "sub": email}

    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return {"access_token": encoded_jwt, "token_type": "bearer"}
