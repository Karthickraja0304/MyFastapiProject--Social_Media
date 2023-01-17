"""add remaining columns to posts 

Revision ID: 5d4580158a41
Revises: 7c5ab9f937c6
Create Date: 2022-12-24 19:35:38.231649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d4580158a41'
down_revision = '7c5ab9f937c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("location", sa.String(), nullable = False))
    op.add_column("posts", sa.Column("published", sa.Boolean(), server_default = "True", nullable = False))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                        server_default = sa.text("now()"), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column("posts",'location')
    op.drop_column("posts",'published')
    op.drop_column("posts",'created_at')
    pass
