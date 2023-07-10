from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field('my super secret key', env='OPENAI_API_KEY')
    SERPAPI_API_KEY: str = Field('my super secret key', env='SERPAPI_API_KEY')


    class Config:
        """
        A definition for checking local environment variables
        """

        env_file_encoding = 'utf-8'
        case_sensitive = True
        env_file = '.env'

settings = Settings()
