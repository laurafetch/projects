"""empty message

Revision ID: e76f50e3da1b
Revises: 7c09c5c5412a
Create Date: 2024-07-25 18:01:33.528549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e76f50e3da1b'
down_revision = '7c09c5c5412a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tweet_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['tweet_id'], ['tweets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'tweet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###
