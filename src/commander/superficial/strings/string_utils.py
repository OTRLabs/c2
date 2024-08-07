from __future__ import annotations
from ...configuration.envs import Settings
from rich.console import Console

from rich.table import Table

class StringUtils:
    
    
    async def load_language_based_on_config(self, console: Console, settings: Settings) -> None:
        if settings.base_config.LANGUAGE == "EN_US":
            from .languages.EN_US import EN_US_Strings
            self.strings = EN_US_Strings()
        else:
            raise NotImplementedError("Language not supported")