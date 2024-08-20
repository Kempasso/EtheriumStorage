from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.settings.infura_settings import InfuraSettings
from src.core.settings.postgres_settings import PGSettings
from src.core.settings.redis_settings import RedisSettings


class Settings(BaseSettings):
    postgres_settings: PGSettings = PGSettings()
    infura_settings: InfuraSettings = InfuraSettings()
    redis_settings: RedisSettings = RedisSettings()
