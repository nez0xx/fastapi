from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated
import uvicorn
from contextlib import asynccontextmanager

from catalog import router as catalog_router
from posts import router as posts_router
from users import router as users_router
from groups import router as groups_router
from core.models import db_helper, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(groups_router)
app.include_router(catalog_router)
app.include_router(users_router)
app.include_router(posts_router)




class CreatePost(BaseModel):
    title: str



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
