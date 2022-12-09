"""add content to post table

Revision ID: 91cc08ab1cc1
Revises: f8ca38e81311
Create Date: 2022-12-08 21:35:58.010695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91cc08ab1cc1'
down_revision = 'f8ca38e81311'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass