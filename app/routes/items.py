from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import crud.items as crud
from auth.jwthandler import get_current_user
from schemas.items import ItemInSchema, ItemOutSchema, UpdateItem 
from schemas.token import Status
from schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/notes",
    response_model=List[ItemOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_notes():
    return await crud.get_notes()


@router.get(
    "/note/{note_id}",
    response_model=ItemOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_note(note_id: int) -> ItemOutSchema:
    try:
        return await crud.get_note(note_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist",
        )


@router.post(
    "/notes", response_model=ItemOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_note(
    note: ItemInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> ItemOutSchema:
    return await crud.create_note(note, current_user)


@router.patch(
    "/note/{note_id}",
    dependencies=[Depends(get_current_user)],
    response_model=ItemOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_note(
    note_id: int,
    note: UpdateItem,
    current_user: UserOutSchema = Depends(get_current_user),
) -> ItemOutSchema:
    return await crud.update_note(note_id, note, current_user)


@router.delete(
    "/note/{note_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_note(
    note_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_note(note_id, current_user)