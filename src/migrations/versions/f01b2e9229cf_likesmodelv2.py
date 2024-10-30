"""LikesModelV2

Revision ID: f01b2e9229cf
Revises: f260cb186f9a
Create Date: 2024-10-30 19:15:47.946427

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f01b2e9229cf"
down_revision: Union[str, None] = "f260cb186f9a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "likes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("client_id", sa.Integer(), nullable=True),
        sa.Column("liked_client_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["clients.id"],
        ),
        sa.ForeignKeyConstraint(
            ["liked_client_id"],
            ["clients.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_likes_client_id"), "likes", ["client_id"], unique=False
    )
    op.create_index(op.f("ix_likes_id"), "likes", ["id"], unique=False)
    op.create_index(
        op.f("ix_likes_liked_client_id"),
        "likes",
        ["liked_client_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_likes_liked_client_id"), table_name="likes")
    op.drop_index(op.f("ix_likes_id"), table_name="likes")
    op.drop_index(op.f("ix_likes_client_id"), table_name="likes")
    op.drop_table("likes")
    # ### end Alembic commands ###