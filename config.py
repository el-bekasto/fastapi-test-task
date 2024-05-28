from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Pydantic settings очень удобен для получения настроек из env файла
    """
    DB_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
