"""Core configuration using pydantic BaseSettings.
Loads environment variables from .env file.
"""
import os
from pathlib import Path
from pydantic import BaseSettings, Field, PostgresDsn

class Settings(BaseSettings):
    # Application
    APP_NAME: str = Field("Professeur IA Multilingue", env="APP_NAME")
    DEBUG: bool = Field(True, env="DEBUG")

    # Database
    POSTGRES_SERVER: str = Field(..., env="POSTGRES_SERVER")
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DB")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")

    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=str(self.POSTGRES_PORT),
            path=f"/{self.POSTGRES_DB}",
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
