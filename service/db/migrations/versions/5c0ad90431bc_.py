"""empty message

Revision ID: 5c0ad90431bc
Revises: 
Create Date: 2022-11-17 03:42:18.785019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c0ad90431bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('kind', sa.String(), nullable=True),
    sa.Column('amount', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operations_id'), 'operations', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_operations_id'), table_name='operations')
    op.drop_table('operations')
    # ### end Alembic commands ###