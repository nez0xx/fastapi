from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, User
from . import crud
from users.schemas import UserCreate


router = APIRouter(prefix='/users')

@router.get("/{username}")
async def get_user(username:str, session: AsyncSession = Depends(db_helper.get_scoped_session_dependency)):
    user = await crud.user_by_id(session=session, username=username)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/create")
async def create_post_view( user_in: UserCreate, session: AsyncSession = Depends(db_helper.get_scoped_session_dependency)):
    return await crud.create_user(session=session, user=user_in)

'''
@router.patch("/patch/{post_id}")
async def edit_post_partial(post_edited: PostEdit,
                            session: AsyncSession = Depends(db_helper.get_scoped_session_dependency),
                            post: Post = Depends(product_by_id)):
    return await crud.edit_post(session, post, post_edited, partial=True)
'''