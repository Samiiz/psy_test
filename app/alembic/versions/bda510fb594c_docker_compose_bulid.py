"""docker-compose bulid

Revision ID: bda510fb594c
Revises: 9f8e6d7ec6b2
Create Date: 2024-03-25 07:13:14.749453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bda510fb594c'
down_revision: Union[str, None] = '9f8e6d7ec6b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
