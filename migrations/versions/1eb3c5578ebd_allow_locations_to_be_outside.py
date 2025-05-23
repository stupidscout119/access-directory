"""allow locations to be outside

Revision ID: 1eb3c5578ebd
Revises: 5ffc90638c96
Create Date: 2025-03-13 15:24:45.657431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eb3c5578ebd'
down_revision = '5ffc90638c96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_outside', sa.Boolean(), nullable=False, server_default='FALSE'))
        # https://stackoverflow.com/a/33705698
        # batch_op.alter_column(sa.Column('is_outside',server_default=None))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.drop_column('is_outside')

    # ### end Alembic commands ###
