
"""added balance to account

Revision ID: 97eab3b10728
Revises: 8b038477ba71
Create Date: 2024-03-27 16:15:53.875117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97eab3b10728'
down_revision: Union[str, None] = '8b038477ba71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('balance', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounts', 'balance')
    # ### end Alembic commands ###