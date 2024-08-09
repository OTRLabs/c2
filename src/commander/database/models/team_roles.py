from __future__ import annotations

from enum import Enum, auto


class TeamRoles(Enum):
    """Valid Values for Team Roles."""

    LEADER = auto()
    MEMBER = auto()