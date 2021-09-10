"""Initial migration.

Revision ID: 9363071a8e5e
Revises: 
Create Date: 2021-09-10 15:15:10.383693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9363071a8e5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###