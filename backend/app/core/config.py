from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    app_name: str = "Pearl Mccaffrey"
    owner_name: str = "Pearl Mccaffrey"
    tagline: str = "Personal Shopper"
    database_url: str = "sqlite:///./pearl_atelier.db"
    frontend_dir: Path = Path(__file__).resolve().parents[3] / "frontend"

    class Config:
        env_file = ".env"


settings = Settings()
