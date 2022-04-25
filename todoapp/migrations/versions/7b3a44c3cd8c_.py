"""empty message

Revision ID: 7b3a44c3cd8c
Revises: ee6220681542
Create Date: 2022-04-03 20:57:19.974116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b3a44c3cd8c'
down_revision = 'ee6220681542'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todo', sa.Column('list_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'todo', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###