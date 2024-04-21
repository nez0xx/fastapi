from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Post, User, db_helper
from sqlalchemy import select, Result
from fastapi import Depends, Path
from typing import Annotated


async def product_by_id(session: AsyncSession = Depends(db_helper.get_scoped_session_dependency),
                        post_id: int = Annotated[int, Path]):
    return await session.get(Post, post_id)


async def user_by_id(user_id: int, session: AsyncSession):
    stmt = select(User).where(User.id == user_id)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    return user
