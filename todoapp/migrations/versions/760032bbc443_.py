"""empty message

Revision ID: 760032bbc443
Revises: 
Create Date: 2022-02-17 06:29:09.692204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '760032bbc443'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###