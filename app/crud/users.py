from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import IntegrityError

from database.models import Users
from schemas.users import UserOutSchema
from schemas.token import Status


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_users():
    # TODO: check if user is admin
    return await UserOutSchema.from_queryset(Users.all())

async def get_user(user_id): 
    # TODO: check if user is admin
    return await UserOutSchema.from_queryset_single(Users.get(id=user_id))

# TODO: add typing
async def create_user(user) -> UserOutSchema:
    user.password = pwd_context.encrypt(user.password)

    try:
        user_obj = await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(status_code=401, detail=f"Sorry, that username already exists.")

    return await UserOutSchema.from_tortoise_orm(user_obj)


async def delete_user(user_id, current_user) -> Status:

    # TODO: why user_id?
    # get user from db for the given user_id
    try:
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    # if the same user id is found,  delete the user - only the logged in user can delete their own account
    if db_user.id == current_user.id:
        deleted_count = await Users.filter(id=user_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        return Status(message=f"Deleted user {user_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")