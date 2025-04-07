from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    DATABASE_NAME: str
    app_name: str = "AI Quiz App"
    debug: bool = True
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
