from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str
    database_name: str
    app_name: str = "AI Quiz App"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
