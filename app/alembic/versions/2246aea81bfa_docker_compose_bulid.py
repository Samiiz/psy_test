"""docker-compose bulid

Revision ID: 2246aea81bfa
Revises: 4cd0b225a6e8
Create Date: 2024-03-24 21:34:21.119122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2246aea81bfa'
down_revision: Union[str, None] = '4cd0b225a6e8'
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
