from __future__ import annotations

class BaseApplicationConfiguration:
    LANGUAGE: str = "EN_US"


class Settings:
    base_config: BaseApplicationConfiguration = BaseApplicationConfiguration()