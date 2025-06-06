"""init

Revision ID: 5814523aa0cb
Revises: 
Create Date: 2025-04-23 11:13:37.761362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5814523aa0cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###
