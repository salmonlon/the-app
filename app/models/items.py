from pydantic.dataclasses import dataclass
from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from pydantic import BaseModel

@dataclass
class ItemBase:
    """Item dataclass

    Args:
        BaseModel (BaseModel): _description_
    """
    name: str
    description: Optional[str] = None
