"""new fields in user model

Revision ID: 5aeb6b8befe2
Revises: 7cd25a326f25
Create Date: 2019-11-15 12:23:00.748971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aeb6b8befe2'
down_revision = '7cd25a326f25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
