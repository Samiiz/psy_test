"""docker-compose bulid

Revision ID: 9f8e6d7ec6b2
Revises: 0b8ee875b6e2
Create Date: 2024-03-25 07:10:17.094100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f8e6d7ec6b2'
down_revision: Union[str, None] = '0b8ee875b6e2'
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
