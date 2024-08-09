from __future__ import annotations






from typing import List, Optional




from datetime import date, datetime
from typing import TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:

    from .team_member import TeamMember
    from .user_role import UserRole
    from .xmpp_encryption_methods import XMPPEncryptionMethods




class User(UUIDAuditBase):
    __tablename__: str = "user_account"
    __table_args__ = {"comment": "User account for the commander application, handles authentication and authorization"}
    pii_columns: List[str] = ["email", "phone_number"]

    # User account information
    xmpp_address: Mapped[str] = mapped_column(String(255), nullable=True, comment="The XMPP address for the user")
    xmpp_encryption_method: Mapped[bool[XMPPEncryptionMethods]] = mapped_column(String(255), nullable=False, comment="The XMPP encryption method for the user")    
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="The name of the user")
    username: Mapped[str] = mapped_column(String(255), nullable=False, comment="The username of the user")
    login_name: Mapped[str] = mapped_column(String(255), nullable=False, comment="The login name of the user")
    
    # User account security information
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False, comment="The hash of the user's password")
    password_salt: Mapped[str] = mapped_column(String(255), nullable=False, comment="The salt used to hash the user's password")
    
    
    # user status
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, comment="Whether the user is active or not")
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, comment="Whether the user is deleted or not")
    is_xmpp_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, comment="Whether the user's XMPP address is verified or not")
        
