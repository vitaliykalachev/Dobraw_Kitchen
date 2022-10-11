"""add user table

Revision ID: e9844435faca
Revises: 4232dfd97bd6
Create Date: 2022-09-20 21:44:02.526191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9844435faca'
down_revision = '4232dfd97bd6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id',  sa.Integer(),  nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True), 
                              server_default=sa.text('now()'), nullable=False, ),
                    sa.PrimaryKeyConstraint('id'), 
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
