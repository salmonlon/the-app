from http.client import HTTPException
from fastapi import APIRouter, Depends

from models.items import Item
from dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

fake_items_db = {
        "plumbus": {
            "name": "Plumbus"
            }, 
        "gun": {
            "name": "Portal Gun"
            }
    }


@router.get('/{item_id}')
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"]}

@router.post('')
async def create_item(item: Item):
    return {"item_name": item.name, "item_description": item.description}
