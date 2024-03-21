"""empty message

Revision ID: ceec50efa0f4
Revises: e275d5d4b741
Create Date: 2024-03-21 16:21:47.771998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceec50efa0f4'
down_revision: Union[str, None] = 'e275d5d4b741'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advertisement__ad_booking_available',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('ad_booking_available_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ad_booking_available_id'], ['ad_booking_available.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['advertisement.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'ad_booking_available_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('advertisement__ad_booking_available')
    # ### end Alembic commands ###