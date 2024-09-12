"""add user_id to Spaces
Revision ID: acb5adb325a9
Revises: 0ba68e5351dc
Create Date: 2024-07-23 12:54:57.545266
"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic
revision = 'acb5adb325a9'
down_revision = '0ba68e5351dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spaces', sa.Column('user_id', sa.UUID(), nullable=True))
    op.alter_column(
        'spaces', 'embedding_model_id', existing_type=sa.UUID(), nullable=True
    )
    op.create_unique_constraint(None, 'spaces', ['user_id'])
    op.create_foreign_key(
        None, 'spaces', 'users', ['user_id'], ['id'], ondelete='CASCADE'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'spaces', type_='foreignkey')
    op.drop_constraint(None, 'spaces', type_='unique')
    op.alter_column(
        'spaces', 'embedding_model_id', existing_type=sa.UUID(), nullable=False
    )
    op.drop_column('spaces', 'user_id')
    # ### end Alembic commands ###