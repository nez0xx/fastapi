from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Group


async def group_by_id(group_id: int, session: AsyncSession):
    stmt = select(Group).where(Group.id == group_id)
    result: Result = await session.execute(stmt)
    group: Group | None = result.scalar_one_or_none()
    return group