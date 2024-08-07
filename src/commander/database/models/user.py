from __future__ import annotations






from typing import List, Optional




from datetime import date, datetime
from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:

    from .team_member import TeamMember
    from .user_role import UserRole


class User(UUIDAuditBase):
    __tablename__: str = "user_account"
    __table_args__ = {"comment": "User account for the commander application, handles authentication and authorization"}


