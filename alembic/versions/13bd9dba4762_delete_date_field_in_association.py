"""delete date field in association

Revision ID: 13bd9dba4762
Revises: fcd4dd7871da
Create Date: 2024-04-21 18:34:05.713034

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13bd9dba4762'
down_revision: Union[str, None] = 'fcd4dd7871da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_group_association', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_group_association', sa.Column('date', sa.VARCHAR(), nullable=False))
    # ### end Alembic commands ###
