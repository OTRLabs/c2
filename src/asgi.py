from __future__ import annotations

import asyncio

from rich.console import Console
from rich.prompt import Prompt
from datetime import datetime
from commander.application import create_app





async def main() -> None:

    console: Console = Console()    

    console.print(f"Initializing your commander environment", style="bold green")

    app = await create_app(console=console)
    
    return app



if __name__ == "__main__":
    asyncio.run(main())





    