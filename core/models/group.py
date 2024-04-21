from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.models import User
    from core.models import UserGroupAssociation


class Group(Base):
    name: Mapped[str]
    description: Mapped[str]
    users: Mapped[list["User"]] = relationship(secondary="user_group_association", back_populates="groups")
'''
AWarning: relationship 'User.groups_details' will copy column users.id to column user_group_association.user_id, which conflicts with relationship(s): 'User.groups' (copies users.id to user_group_association.user_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="groups"' to the 'User.groups_details' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)
  selectinload(User.groups),
'''

