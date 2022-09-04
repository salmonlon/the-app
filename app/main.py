# import time
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from tomlkit import item
from tortoise import Tortoise

# from dependencies import get_query_token
# from routers import items
from database.register import register_tortoise
from database.config import TORTOISE_ORM
from routes import users, notes

# enable schemas to read relationship between models
Tortoise.init_models(['database.models'], 'models')


app = FastAPI(
    # dependencies=[Depends(get_query_token)]
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
)

# routes
app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

# @app.middleware("http")
# async def add_process_time_header(request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


@app.get("/")
async def doc_redirect():
    return RedirectResponse(url='/docs')
