from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    jwt_secret: str
    jwt_alghoritm: str = "HS256"
    token_minutes: int = 30
    cors_origins: list[str] = ["http://localhost:3000"]
    admin_email: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_prefix="")

settings = Settings