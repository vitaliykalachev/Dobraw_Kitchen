"""add content column to posts table

Revision ID: 4232dfd97bd6
Revises: b35d7ff3a9c2
Create Date: 2022-09-20 21:34:28.927528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4232dfd97bd6'
down_revision = 'b35d7ff3a9c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
