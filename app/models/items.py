
from dataclasses import dataclass

from pydantic import BaseModel

@dataclass
class Item(BaseModel):
    id: int
    name: str
    description: str