from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    redis_host: str = Field(validation_alias="REDIS_HOST")
    redis_port: int = Field(validation_alias="REDIS_PORT")

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/"

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
