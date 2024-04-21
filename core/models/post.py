from typing import TYPE_CHECKING
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from core.models import User


class Post(Base):
    title: Mapped[str]
    text: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped['User'] = relationship("User", back_populates="posts")
