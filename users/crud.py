from core.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from .schemas import UserCreate


async def create_user(session: AsyncSession, user: UserCreate):
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    return user


async def user_by_id(session: AsyncSession, username: str):
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    return user



