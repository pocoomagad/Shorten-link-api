from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_PORT: int
    APP_HOST: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PLUGIN: str 
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USER: str
    REDIS_PASSWORD: str
    REDIS_DB: str


settings = Settings()

BASE_URL = f"http://{settings.APP_HOST}:{settings.APP_PORT}"
POSTGRES_URL = f"postgresql+{settings.POSTGRES_PLUGIN}://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
REDIS_URL = f"redis://{settings.REDIS_USER}:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DB}"