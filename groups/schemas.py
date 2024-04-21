from pydantic import BaseModel


class GroupCreate(BaseModel):
    name: str
    description: str
class AddFollower(BaseModel):
    group_id: int
    user_id: int

