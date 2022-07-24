from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import crud.users as crud
from auth.users import validate_user
from schemas.token import Status
from schemas.users import UserInSchema, UserOutSchema

from auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


router = APIRouter()

### AUTHENTICATION ###
@router.post("/register", response_model=UserOutSchema)
async def create_user(user: UserInSchema) -> UserOutSchema:
    return await crud.create_user(user)


@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False, # set to true in prod
    )

    return response


### GET USER INFO ###
@router.get(
    "/users/whoami", response_model=UserOutSchema, dependencies=[Depends(get_current_user)]
)
async def read_users_me(current_user: UserOutSchema = Depends(get_current_user)):
    return current_user

@router.get(
    "/users", 
    response_model=List[UserOutSchema], 
    dependencies=[Depends(get_current_user)]
)
async def read_all_users():
    return await crud.get_users()

@router.get(
    "/users/{user_id}", 
    response_model=UserOutSchema, 
    dependencies=[Depends(get_current_user)]
)
async def read_user(user_id: int):
    try: 
        return await crud.get_user(user_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404, 
            detail=f"User {user_id} not found"
        )

### DELETE USER ###
@router.delete(
    "/user/{user_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_user(
    user_id: int, current_user: UserOutSchema = Depends(get_current_user)
) -> Status:
    return await crud.delete_user(user_id, current_user)