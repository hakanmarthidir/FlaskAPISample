"""initial migration

Revision ID: c37741b6dcf1
Revises: 4db92c31be5d
Create Date: 2018-09-23 00:48:14.840789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c37741b6dcf1'
down_revision = '4db92c31be5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('studentage', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_students_studentage'), 'students', ['studentage'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_studentage'), table_name='students')
    op.drop_column('students', 'studentage')
    # ### end Alembic commands ###