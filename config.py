from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    sqlalchemy_uri: str
    secret_key: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

