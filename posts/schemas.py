from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    text: str
    user_id: int


class PostCreate(PostBase):
    pass


class Post(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class PostEdit(BaseModel):

    title: str | None = None
    text: str | None = None