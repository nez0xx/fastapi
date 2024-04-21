from core.models import Base, Post
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .group import Group
    from core.models import UserGroupAssociation


class User(Base):
    username: Mapped[str] = mapped_column(String(40), unique=True)
    posts: Mapped[list[Post]] = relationship("Post", back_populates="user")
    groups: Mapped[list["Group"]] = relationship(secondary="user_group_association", back_populates="users")

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username
