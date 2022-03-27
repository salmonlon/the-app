from fastapi import APIRouter, Depends, HTTPException

from models.items import ItemBase
from dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

fake_items_db = {
    
    }


@router.get('/{item_id}')
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    return fake_items_db[item_id]

@router.get('/')
async def read_items():
    return fake_items_db

@router.post('/')
async def create_item(item: ItemBase):
    fake_items_db[item.name] = item
    print(len(fake_items_db))
    return item