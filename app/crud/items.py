from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from database.models import Items 
from schemas.items import ItemOutSchema


async def get_notes():
    return await ItemOutSchema.from_queryset(Items.all())


async def get_note(note_id) -> ItemOutSchema:
    return await ItemOutSchema.from_queryset_single(Items.get(id=note_id))


# TODO: add typing
async def create_note(note, current_user) -> ItemOutSchema:
    note_dict = note.dict(exclude_unset=True)
    note_dict["author_id"] = current_user.id
    note_obj = await Items.create(**note_dict)
    return await ItemOutSchema.from_tortoise_orm(note_obj)


async def update_note(note_id, note, current_user) -> ItemOutSchema:
    try:
        db_note = await ItemOutSchema.from_queryset_single(Items.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")

    if db_note.author.id == current_user.id:
        await Items.filter(id=note_id).update(**note.dict(exclude_unset=True))
        return await ItemOutSchema.from_queryset_single(Items.get(id=note_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_note(note_id, current_user):
    try:
        db_note = await ItemOutSchema.from_queryset_single(Items.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")

    if db_note.author.id == current_user.id:
        deleted_count = await Items.filter(id=note_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
        return f"Deleted note {note_id}"

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")