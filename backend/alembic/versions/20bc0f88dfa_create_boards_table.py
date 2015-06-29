"""create boards table

Revision ID: 20bc0f88dfa
Revises: 
Create Date: 2015-06-29 10:22:35.830972

"""

# revision identifiers, used by Alembic.
revision = '20bc0f88dfa'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'boards',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('shortname', sa.String(10), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('boards')
