from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    GENERATION_DIRECTORY: str = Field("gen", env="GENERATION_DIRECTORY")
    OPENAI_API_BASE: str = Field(None, env="OPENAI_API_BASE")
    OPENAI_API_KEY: str = Field("my super secret key", env="OPENAI_API_KEY")
    OPENAI_TXT_MODEL: str = Field("text-davinci-003", env="OPENAI_TXT_MODEL")
    OPENAI_MAX_TOKENS: int = Field(None, env="OPENAI_MAX_TOKENS")
    OPENAI_CHAT_MODEL: str = Field("gpt-3.5-turbo", env="OPENAI_CHAT_MODEL")
    OPENAI_TEMPERATURE: str = Field(0.0, env="OPENAI_TEMPERATURE")
    SERPAPI_API_KEY: str = Field("my super secret key", env="SERPAPI_API_KEY")

    class Config:
        """
        A definition for checking local environment variables
        """

        env_file_encoding = "utf-8"
        case_sensitive = True
        env_file = ".env"


settings = Settings()
