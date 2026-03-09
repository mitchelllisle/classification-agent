"""Runtime settings for the classification service."""

from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class AnthropicConfig(BaseSettings):
    """Anthropic API configuration settings."""

    model_config = SettingsConfigDict(
        env_prefix="ANTHROPIC_",
    )

    api_key: str = Field(min_length=1)


class Settings(BaseModel):
    """Application settings loaded from environment variables."""

    anthropic: AnthropicConfig = AnthropicConfig()

