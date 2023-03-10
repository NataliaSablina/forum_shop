"""products init

Revision ID: 33925e9a50f7
Revises: 
Create Date: 2023-02-07 14:25:52.520869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33925e9a50f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forum_shop_products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_forum_shop_products_id'), 'forum_shop_products', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_forum_shop_products_id'), table_name='forum_shop_products')
    op.drop_table('forum_shop_products')
    # ### end Alembic commands ###
