"""add content column to posts table 

Revision ID: e7638a154b99
Revises: 53a46df9a30d
Create Date: 2022-12-23 12:48:33.260362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7638a154b99'
down_revision = '53a46df9a30d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable = False ))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
