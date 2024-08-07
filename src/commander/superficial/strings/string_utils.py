# src/commander/superficial/strings/string_utils.py

from __future__ import annotations
from typing import Type
from rich.console import Console
from ...configuration.envs import Settings

class StringUtils:
    def __init__(self):
        self.strings = None

    async def load_language_based_on_config(self, console: Console, settings: Settings) -> None:
        language = settings.LANGUAGE
        try:
            module = __import__(f"commander.superficial.strings.languages.{language}", fromlist=[""])
            self.strings = getattr(module, f"{language}_Strings")()
        except ImportError:
            console.print(f"[bold red]Error:[/bold red] Language '{language}' not supported")
            raise NotImplementedError(f"Language '{language}' not supported")

    def get_strings(self) -> Type[EN_US_Strings]:
        if self.strings is None:
            raise RuntimeError("Strings not loaded. Call load_language_based_on_config first.")
        return self.strings

string_utils = StringUtils()