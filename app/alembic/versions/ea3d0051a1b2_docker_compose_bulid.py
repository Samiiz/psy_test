"""docker-compose bulid

Revision ID: ea3d0051a1b2
Revises: 62b1bdea2c6f
Create Date: 2024-03-24 22:28:36.791655

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea3d0051a1b2'
down_revision: Union[str, None] = '62b1bdea2c6f'
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
