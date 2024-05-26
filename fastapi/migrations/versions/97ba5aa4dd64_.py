"""empty message

Revision ID: 97ba5aa4dd64
Revises: 6b4958b47806
Create Date: 2024-05-16 13:47:49.187215

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97ba5aa4dd64'
down_revision: Union[str, None] = '6b4958b47806'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tariffs', sa.Column('available_ads', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tariffs', 'available_ads')
    # ### end Alembic commands ###