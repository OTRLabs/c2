from aenum import Enum, auto
from __future__ import annotations

class XMPPEncryptionMethods(Enum):
    OMEMO: XMPPEncryptionMethods = auto()
    OTR: XMPPEncryptionMethods = auto()
    
    def __str__(self) -> str:
        return self.name
    
    async def __aiter__(self) -> XMPPEncryptionMethods:
        return self
    
    async def __anext__(self) -> XMPPEncryptionMethods:
        raise StopAsyncIteration

    async def __aenter__(self) -> XMPPEncryptionMethods:
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        pass
