# src/asgi.py

from __future__ import annotations

import asyncio
import logging
from typing import Any

from rich.console import Console
from rich.logging import RichHandler
from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyPlugin
from commander.application import create_app
from commander.configuration.envs import Settings
from commander.superficial.strings.string_utils import string_utils

# Set up logging
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger("rich")

async def main() -> Litestar:
    console: Console = Console()    
    
    # Load language strings
    await string_utils.load_language_based_on_config(console, Settings)
    strings = string_utils.get_strings()

    strings.get_welcome_message(console)

    # Create the application
    app = await create_app(console=console, settings=Settings)
    
    # Add SQLAlchemy plugin
    app.register_plugin(SQLAlchemyPlugin())

    return app

def run_development_server() -> None:
    import uvicorn
    
    log.info("Starting development server...")
    uvicorn.run(
        "asgi:main",
        host="0.0.0.0",
        port=8000,
        reload=True,
        factory=True
    )

if __name__ == "__main__":
    run_development_server()