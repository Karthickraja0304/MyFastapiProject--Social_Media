"""add foreign key to post table

Revision ID: 7c5ab9f937c6
Revises: c18971fcc6bd
Create Date: 2022-12-24 18:43:39.184811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c5ab9f937c6'
down_revision = 'c18971fcc6bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("owner_id",sa.Integer(), nullable = False))
    op.create_foreign_key("post_users_fk", source_table= "posts", referent_table= "users",
                        local_cols=["owner_id"], remote_cols=['id'], ondelete= "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts","owner_id")
    pass
