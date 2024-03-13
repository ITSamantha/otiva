"""empty message

Revision ID: 8b15f6a0a619
Revises: 00236b9853e9
Create Date: 2024-03-13 13:33:15.672409

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b15f6a0a619'
down_revision: Union[str, None] = '00236b9853e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('advertisement__category')
    op.alter_column('address', 'country_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('address', 'city_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('address', 'street',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('address', 'house',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.drop_column('address', 'address')
    op.add_column('advertisement', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'advertisement', 'category', ['category_id'], ['id'])
    op.drop_constraint('chat_message_attachements_chat_message_id_fkey', 'chat_message_attachements', type_='foreignkey')
    op.create_foreign_key(None, 'chat_message_attachements', 'chat_messages', ['chat_message_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chat_message_attachements', type_='foreignkey')
    op.create_foreign_key('chat_message_attachements_chat_message_id_fkey', 'chat_message_attachements', 'chats', ['chat_message_id'], ['id'])
    op.drop_constraint(None, 'advertisement', type_='foreignkey')
    op.drop_column('advertisement', 'category_id')
    op.add_column('address', sa.Column('address', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.alter_column('address', 'house',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('address', 'street',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('address', 'city_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('address', 'country_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_table('advertisement__category',
    sa.Column('advertisement_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['advertisement_id'], ['advertisement.id'], name='advertisement__category_advertisement_id_fkey'),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='advertisement__category_category_id_fkey'),
    sa.PrimaryKeyConstraint('advertisement_id', 'category_id', name='advertisement__category_pkey')
    )
    # ### end Alembic commands ###
