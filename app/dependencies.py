from fastapi import Header, HTTPException

async def get_token_header(x_token: str = Header(...)):
    # TODO: use https://fastapi.tiangolo.com/tutorial/security/
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    print('getting token header')
    return {"x_token": x_token}

async def get_query_token(token: str):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="token query param invalid")