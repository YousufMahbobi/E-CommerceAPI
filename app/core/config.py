from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False

    class Config:
        env_file = BASE_DIR / ".env"

settings = Settings()


