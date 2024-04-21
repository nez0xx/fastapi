from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


if TYPE_CHECKING:
    from core.models import User, Group


class UserGroupAssociation(Base):

    __tablename__ = "user_group_association"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "group_id",
            name="idx_unique_user_group",
        ),
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    #date: Mapped[str]

