"""add last few columns to posts table

Revision ID: e970f1c99c59
Revises: 25108e856176
Create Date: 2022-09-26 17:02:26.908760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e970f1c99c59'
down_revision = '25108e856176'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column(
        'create_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
    ('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'create_at')
    
    pass

