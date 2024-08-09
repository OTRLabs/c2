from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from advanced_alchemy.base import SlugKey, UUIDAuditBase, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from .xmpp_encryption_methods import XMPPEncryptionMethods
    from .user import User
    
    
class XMPPAddress(UUIDAuditBase, SlugKey):
    """XMPP Address."""
    
    __tablename__ = "xmpp_address"
    
    address: Mapped[str] = mapped_column(unique=True)
    encryption_method: Mapped[str[XMPPEncryptionMethods]] = mapped_column(nullable=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user_account.id", ondelete="cascade"))
    
    # -----------
    # ORM Relationships
    # ------------
    user: Mapped[User] = relationship(foreign_keys="XMPPAddress.user_id", lazy="noload")