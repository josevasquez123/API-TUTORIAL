"""create posts table

Revision ID: d3b24146519c
Revises: 
Create Date: 2022-12-08 20:59:44.644211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3b24146519c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key = True),
    sa.Column('title', sa.String(), nullable = False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
