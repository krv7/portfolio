"""empty message

Revision ID: b8c315250e13
Revises: 8111656fac42
Create Date: 2021-04-05 13:07:38.131343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8c315250e13'
down_revision = '8111656fac42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_blog_cat', table_name='blog')
    op.create_index(op.f('ix_blog_cat'), 'blog', ['cat'], unique=False)
    op.drop_index('ix_blog_content', table_name='blog')
    op.create_index(op.f('ix_blog_content'), 'blog', ['content'], unique=False)
    op.drop_index('ix_blog_description', table_name='blog')
    op.create_index(op.f('ix_blog_description'), 'blog', ['description'], unique=False)
    op.drop_index('ix_blog_title', table_name='blog')
    op.create_index(op.f('ix_blog_title'), 'blog', ['title'], unique=False)
    op.drop_index('ix_project_cat', table_name='project')
    op.create_index(op.f('ix_project_cat'), 'project', ['cat'], unique=False)
    op.drop_index('ix_project_content', table_name='project')
    op.create_index(op.f('ix_project_content'), 'project', ['content'], unique=False)
    op.drop_index('ix_project_description', table_name='project')
    op.create_index(op.f('ix_project_description'), 'project', ['description'], unique=False)
    op.drop_index('ix_project_title', table_name='project')
    op.create_index(op.f('ix_project_title'), 'project', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_title'), table_name='project')
    op.create_index('ix_project_title', 'project', ['title'], unique=1)
    op.drop_index(op.f('ix_project_description'), table_name='project')
    op.create_index('ix_project_description', 'project', ['description'], unique=1)
    op.drop_index(op.f('ix_project_content'), table_name='project')
    op.create_index('ix_project_content', 'project', ['content'], unique=1)
    op.drop_index(op.f('ix_project_cat'), table_name='project')
    op.create_index('ix_project_cat', 'project', ['cat'], unique=1)
    op.drop_index(op.f('ix_blog_title'), table_name='blog')
    op.create_index('ix_blog_title', 'blog', ['title'], unique=1)
    op.drop_index(op.f('ix_blog_description'), table_name='blog')
    op.create_index('ix_blog_description', 'blog', ['description'], unique=1)
    op.drop_index(op.f('ix_blog_content'), table_name='blog')
    op.create_index('ix_blog_content', 'blog', ['content'], unique=1)
    op.drop_index(op.f('ix_blog_cat'), table_name='blog')
    op.create_index('ix_blog_cat', 'blog', ['cat'], unique=1)
    # ### end Alembic commands ###