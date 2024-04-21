from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.models import UserGroupAssociation, Group, User
from sqlalchemy.ext.asyncio import AsyncSession
from groups.dependencies import group_by_id
from posts.dependencies import user_by_id
from .schemas import GroupCreate


async def create_group(session: AsyncSession, group_in: GroupCreate):
    print("#"*1000)
    group = Group(**group_in.model_dump())
    print("*"*1000)
    session.add(group)
    await session.commit()
    return group


async def add_follower(session: AsyncSession, user_id: int, group_id: int):
    user = await session.scalar(
        select(User)
        .where(User.id == user_id)
        .options(
            selectinload(User.groups),
        ),
    )
    group = await session.scalar(
        select(Group)
        .where(Group.id == group_id)
        .options(
            selectinload(Group.users),
        ),
    )
    user.groups.append(group)
    await session.commit()

    for user in group.users:
        print(user.username)
        print('sadf')
    return group.id

async def followers_list(session: AsyncSession, group_id: int):
    group = await session.scalar(
        select(Group)
        .where(Group.id == group_id)
        .options(
            selectinload(Group.users),
        ),
    )
    for user in group.users:
        print(user)

    return group.users