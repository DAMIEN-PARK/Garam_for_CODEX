"""add_commit_status_chat_session_insight

Revision ID: 20260116add1
Revises: c750f08ac421
Create Date: 2026-01-16 12:30:00.000000

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "20260116add1"
down_revision: Union[str, Sequence[str], None] = "c750f08ac421"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "chk_chat_s_insight_status", "chat_session_insight", type_="check"
    )
    op.create_check_constraint(
        "chk_chat_s_insight_status",
        "chat_session_insight",
        "status IN ('success','failed','commit')",
    )


def downgrade() -> None:
    op.drop_constraint(
        "chk_chat_s_insight_status", "chat_session_insight", type_="check"
    )
    op.create_check_constraint(
        "chk_chat_s_insight_status",
        "chat_session_insight",
        "status IN ('success','failed')",
    )
