import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    development: bool = True
    log_level: str = "INFO"
    no_access_log: bool = False
    use_colors: bool = True

    backend: str ="sqlite"
    db_url: str = "sqlite:///./terraformregistryapi.db"

    class Config:
        env_prefix = 'REGISTRY_'

Config = Settings()