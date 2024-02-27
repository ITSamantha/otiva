"""empty message

Revision ID: cf02c79e2f8a
Revises: e449c91a5167
Create Date: 2024-02-27 18:46:56.766399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf02c79e2f8a'
down_revision: Union[str, None] = 'e449c91a5167'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'date')
    # ### end Alembic commands ###
