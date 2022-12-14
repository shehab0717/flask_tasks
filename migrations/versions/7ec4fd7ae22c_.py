"""empty message

Revision ID: 7ec4fd7ae22c
Revises: 5dd7aa36cdbb
Create Date: 2022-11-07 16:11:23.063803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ec4fd7ae22c'
down_revision = '5dd7aa36cdbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('author')
    # ### end Alembic commands ###
