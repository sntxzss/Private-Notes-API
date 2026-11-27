from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.security import decode_access_token
from app.services import get_user_by_email
oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

