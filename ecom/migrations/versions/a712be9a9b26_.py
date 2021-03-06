"""empty message

Revision ID: a712be9a9b26
Revises: 
Create Date: 2019-02-25 13:52:17.006436

"""
from alembic import op
import sqlalchemy as sa
from ecom.models import custom_datatypes


# revision identifiers, used by Alembic.
revision = 'a712be9a9b26'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('mobile', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.Enum('MALE', 'FEMALE', 'OTHER', name='gender'), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('shipping_address', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accounts_created_at'), 'accounts', ['created_at'], unique=False)
    op.create_index(op.f('ix_accounts_email'), 'accounts', ['email'], unique=False)
    op.create_index(op.f('ix_accounts_mobile'), 'accounts', ['mobile'], unique=False)
    op.create_index(op.f('ix_accounts_username'), 'accounts', ['username'], unique=False)
    op.create_table('product_categories',
    sa.Column('id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_categories_created_at'), 'product_categories', ['created_at'], unique=False)
    op.create_table('carts',
    sa.Column('id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('account_id', custom_datatypes.UUID(length=36), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_carts_created_at'), 'carts', ['created_at'], unique=False)
    op.create_table('product_subcategories',
    sa.Column('id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('product_category_id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['product_category_id'], ['product_categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_subcategories_created_at'), 'product_subcategories', ['created_at'], unique=False)
    op.create_table('products',
    sa.Column('id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('product_subcategory_id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('available_item_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_subcategory_id'], ['product_subcategories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_created_at'), 'products', ['created_at'], unique=False)
    op.create_table('items',
    sa.Column('id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('modified_at', sa.DateTime(), nullable=False),
    sa.Column('product_id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('cart_id', custom_datatypes.UUID(length=36), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_created_at'), 'items', ['created_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_items_created_at'), table_name='items')
    op.drop_table('items')
    op.drop_index(op.f('ix_products_created_at'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_product_subcategories_created_at'), table_name='product_subcategories')
    op.drop_table('product_subcategories')
    op.drop_index(op.f('ix_carts_created_at'), table_name='carts')
    op.drop_table('carts')
    op.drop_index(op.f('ix_product_categories_created_at'), table_name='product_categories')
    op.drop_table('product_categories')
    op.drop_index(op.f('ix_accounts_username'), table_name='accounts')
    op.drop_index(op.f('ix_accounts_mobile'), table_name='accounts')
    op.drop_index(op.f('ix_accounts_email'), table_name='accounts')
    op.drop_index(op.f('ix_accounts_created_at'), table_name='accounts')
    op.drop_table('accounts')
    # ### end Alembic commands ###
