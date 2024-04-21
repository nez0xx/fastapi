from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from groups.schemas import AddFollower, GroupCreate


router = APIRouter(prefix='/groups')

@router.post("/create")
async def create_group(group: GroupCreate, session: AsyncSession = Depends(db_helper.get_scoped_session_dependency)):
    return await crud.create_group(session, group)

@router.post("/add_follower")
async def add_follower(info:AddFollower, session: AsyncSession = Depends(db_helper.get_scoped_session_dependency)):
    return await crud.add_follower(session, info.user_id, info.group_id)

@router.get('/followers')
async def show_followers(group_id: int, session: AsyncSession = Depends(db_helper.get_scoped_session_dependency)):
    return await crud.followers_list(session, group_id)
