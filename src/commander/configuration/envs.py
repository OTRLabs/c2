# src/commander/configuration/envs.py

from __future__ import annotations
from pydantic import BaseSettings, Field
from typing import Optional

class BaseApplicationConfiguration(BaseSettings):
    LANGUAGE: str = Field(default="EN_US", env="COMMANDER_LANGUAGE")
    DEBUG: bool = Field(default=False, env="COMMANDER_DEBUG")
    SECRET_KEY: str = Field(..., env="COMMANDER_SECRET_KEY")
    DATABASE_URL: str = Field(..., env="COMMANDER_DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_environment_variables() -> BaseApplicationConfiguration:
    return BaseApplicationConfiguration()

Settings = get_environment_variables()