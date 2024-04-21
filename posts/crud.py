from core.models import Post
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from .schemas import PostCreate, PostEdit


async def get_posts(session: AsyncSession):
    stmt = select(Post).order_by(Post.id)
    result: Result = await session.execute(stmt)
    posts = result.scalars().all()
    return list(posts)


async def get_post(session: AsyncSession, post_id: int):
    return await session.get(Post, post_id)


async def create_post(session: AsyncSession, post: PostCreate) -> Post:
    post: Post = Post(**post.model_dump())
    session.add(post)
    await session.commit()
    return post


async def edit_post(session: AsyncSession, post: Post, post_edited: PostEdit, partial=False):
    for key, value in post_edited.model_dump(exclude_unset=partial).items():
        setattr(post, key, value)
    await session.commit()
    return post
