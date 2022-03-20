from fastapi import Depends, FastAPI
from dependencies import get_query_token
from routers import items


app = FastAPI(
    # dependencies=[Depends(get_query_token)]
    )
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
