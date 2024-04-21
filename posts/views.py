from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Post
from . import crud
from posts.schemas import PostCreate, PostEdit
from posts.dependencies import product_by_id, user_by_id


router = APIRouter(prefix='/posts')

@router.get("/all")
async def get_all_posts(session: AsyncSession = Depends(db_helper.get_scoped_session_dependency)):
    return await crud.get_posts(session=session)



@router.post("/create")
async def create_post_view(post_in: PostCreate, session: AsyncSession = Depends(db_helper.get_scoped_session_dependency)):

    user = await user_by_id(user_id=post_in.user_id, session=session)
    if user is None:
        raise HTTPException(status_code=404, detail="User bot found")

    return await crud.create_post(session=session, post=post_in)

@router.patch("/patch/{post_id}")
async def edit_post_partial(post_edited: PostEdit,
                            session: AsyncSession = Depends(db_helper.get_scoped_session_dependency),
                            post: Post = Depends(product_by_id)):
    return await crud.edit_post(session, post, post_edited, partial=True)