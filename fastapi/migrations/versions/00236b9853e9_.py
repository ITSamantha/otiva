"""empty message

Revision ID: 00236b9853e9
Revises: 8b751e2e9c52
Create Date: 2024-03-10 17:08:31.887340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00236b9853e9'
down_revision: Union[str, None] = '8b751e2e9c52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chats',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chat_message_attachements',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_message_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_message_id'], ['chats.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chat_users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chat_messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('chat_user_id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('seen_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], ),
    sa.ForeignKeyConstraint(['chat_user_id'], ['chat_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chat_messages')
    op.drop_table('chat_users')
    op.drop_table('chat_message_attachements')
    op.drop_table('chats')
    # ### end Alembic commands ###
