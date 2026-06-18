from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # UI
    UI_BASE_URL: str = "https://practice.expandtesting.com"
    UI_HEADLESS: bool = True
    UI_TIMEOUT: int = 10000

    # UI test user
    UI_USERNAME: str
    UI_PASSWORD: str

    # API
    API_BASE_URL: str = "https://practice.expandtesting.com/notes/api"
    API_TIMEOUT: int = 10000

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

config = Config()
