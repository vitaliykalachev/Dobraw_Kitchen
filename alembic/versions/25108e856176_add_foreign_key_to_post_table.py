"""add foreign key to post_table

Revision ID: 25108e856176
Revises: e9844435faca
Create Date: 2022-09-26 16:56:17.407480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25108e856176'
down_revision = 'e9844435faca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=["user_id"], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column("posts", "user_id")
    pass
