"""Create Price table

Revision ID: 43571a31006d
Revises: 01907c7134ee
Create Date: 2023-11-12 18:27:49.656734

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "43571a31006d"
down_revision: Union[str, None] = "01907c7134ee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "prices",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_code", sa.String(), nullable=True),
        sa.Column("price", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("currency", sa.String(length=3), nullable=True),
        sa.Column("location_osm_id", sa.BigInteger(), nullable=True),
        sa.Column("location_osm_type", sa.String(length=255), nullable=True),
        sa.Column("date", sa.Date(), nullable=True),
        sa.Column("owner", sa.String(), nullable=True),
        sa.Column(
            "created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_prices_id"), "prices", ["id"], unique=False)
    op.create_index(
        op.f("ix_prices_location_osm_id"), "prices", ["location_osm_id"], unique=False
    )
    op.create_index(
        op.f("ix_prices_product_code"), "prices", ["product_code"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_prices_product_code"), table_name="prices")
    op.drop_index(op.f("ix_prices_location_osm_id"), table_name="prices")
    op.drop_index(op.f("ix_prices_id"), table_name="prices")
    op.drop_table("prices")
    # ### end Alembic commands ###
