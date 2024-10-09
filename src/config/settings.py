from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Clean Architecture"
    DEBUG: bool = False
    DATABASE_URL: str

    class Config:
        env_file = ".env"