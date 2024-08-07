from __future__ import annotations
from typing import List, Optional
from datetime import date, datetime

from rich.console import Console

from litestar import Litestar




async def create_app(console: Console) -> Litestar:

    console.print(f"Initializing your commander environment", style="bold green")

    base_app: Litestar = Litestar(
        
    )












