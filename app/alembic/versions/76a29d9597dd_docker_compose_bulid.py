"""docker-compose bulid

Revision ID: 76a29d9597dd
Revises: 5fe1a0e868be
Create Date: 2024-03-24 22:39:21.324461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76a29d9597dd'
down_revision: Union[str, None] = '5fe1a0e868be'
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
