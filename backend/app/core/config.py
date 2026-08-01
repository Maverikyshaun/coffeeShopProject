from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    app_name: str = "Caffè Bruno"
    owner_name: str = "Caffè Bruno"
    tagline: str = "Coffee House & Roastery"
    database_url: str = "sqlite:///./caffe_bruno.db"
    frontend_dir: Path = Path(__file__).resolve().parents[3] / "frontend"

    class Config:
        env_file = ".env"


settings = Settings()
