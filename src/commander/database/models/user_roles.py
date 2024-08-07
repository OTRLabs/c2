from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from enum import Enum


class UserRole(str, Enum):
    ADMIN: str = "ADMIN"
    MANAGER: str = "MANAGER"
    OPERATOR: str = "OPERATOR"
    SPECTATOR: str = "SPECTATOR"
    