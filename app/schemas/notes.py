from typing import Optional

from pydantic import BaseModel
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from database.models import Notes

# early initialise the ORM models with foreign key relations,
# otherwise the foreign key column will not be available in the models
Tortoise.init_models(['database.models'], 'models')
NoteInSchema = pydantic_model_creator(
    Notes, name="NoteIn", exclude=["author_id"], exclude_readonly=True)
NoteOutSchema = pydantic_model_creator(
    Notes, name="Note", exclude =[
      "modified_at", 
      "author.password", 
      "author.created_at", 
      "author.modified_at"
    ]
)

class UpdateNote(BaseModel):
    title: Optional[str]
    content: Optional[str]
    status: Optional[str]