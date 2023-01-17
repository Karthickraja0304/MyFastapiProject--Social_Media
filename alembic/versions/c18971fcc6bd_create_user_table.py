
"""create_user_table

Revision ID: c18971fcc6bd
Revises: e7638a154b99
Create Date: 2022-12-24 12:22:47.866215

"""
from alembic import op
import sqlalchemy as sa
#from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision = 'c18971fcc6bd'
down_revision = 'e7638a154b99'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column('id',sa.Integer(),nullable = False),
                    sa.Column('email',sa.String(),nullable = False),
                    sa.Column('password',sa.String(),nullable = False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable = False, server_default = sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
