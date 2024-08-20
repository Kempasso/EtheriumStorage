from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class InfuraSettings(BaseSettings):
    infura_ws_domain: str = Field(validation_alias="INFURA_WS_DOMAIN")
    infura_api_token: str = Field(validation_alias="INFURA_API_TOKEN")
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
