"""Lol

Revision ID: a94f302adb79
Revises: 030daea92d34
Create Date: 2018-11-19 11:34:38.063090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a94f302adb79'
down_revision = '030daea92d34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'num')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('num', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
