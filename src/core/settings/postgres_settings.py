from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PGSettings(BaseSettings):
    postgres_password: str = Field(validation_alias="POSTGRES_PASSWORD")
    postgres_user: str = Field(validation_alias="POSTGRES_USER")
    postgres_port: int = Field(validation_alias="POSTGRES_PORT")
    postgres_db: str = Field(validation_alias="POSTGRES_DB")
    postgres_host: str = Field(validation_alias="POSTGRES_HOST")

    @property
    def postgres_async_url(self) -> str:
        return (f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@"
                f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}")

    @property
    def postgres_sync_url(self) -> str:
        return (f"postgresql://{self.postgres_user}:{self.postgres_password}@"
                f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}")

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
