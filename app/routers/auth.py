from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.deps import CurrentUser
from app.schemas import Token, UserCreate, UserRead
from app.security import create_access_token
from app.services import authenticate_user, register_user

router = APIRouter(tags=["auth"])

@router.post("/auth/register", status_code=201, response_model=UserRead)
def register(user: UserCreate):
    return register_user(user.email, user.password)

@router.post("/auth/login", response_model=Token)
def login(form: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form.username, form.password)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(subject=user["email"])
    return Token(access_token=token)

@router.get("/me", response_model=UserRead)
def me(current_user: CurrentUser):
    return current_user