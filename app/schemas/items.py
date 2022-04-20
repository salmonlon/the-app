from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from database.models import Items

# for creating new item
NoteInSchema = pydantic_model_creator(
    Items, name="ItemIn", exclude=["author_id"], exclude_readonly=True)

# for retrieving item
NoteOutSchema = pydantic_model_creator(
    Items, name="Item", exclude =[
        "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateNote(BaseModel):
    title: Optional[str]
    content: Optional[str]