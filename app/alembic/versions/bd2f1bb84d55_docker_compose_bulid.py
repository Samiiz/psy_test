"""docker-compose bulid

Revision ID: bd2f1bb84d55
Revises: 3adc5ffb6c42
Create Date: 2024-03-24 21:59:00.794751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd2f1bb84d55'
down_revision: Union[str, None] = '3adc5ffb6c42'
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
