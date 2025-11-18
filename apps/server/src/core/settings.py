from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine.url import URL

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="apps/server/.env", env_file_encoding="utf-8")

    # Snowflake Settings
    SNOWFLAKE_USER: str = ""
    SNOWFLAKE_PASSWORD: str = ""
    SNOWFLAKE_ACCOUNT: str = ""
    SNOWFLAKE_WAREHOUSE: str = ""
    SNOWFLAKE_DATABASE: str = ""
    SNOWFLAKE_SCHEMA: str = ""

    # Redis Settings
    REDIS_HOST: str = ""
    REDIS_PORT: int = 0

    # JWT Settings
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = ""
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 0

    @property
    def snowflake_url(self) -> URL:
        """
        Dynamically construct the SQLAlchemy 2.0 URL object from the settings.
        """
        return URL.create(
            drivername="snowflake",
            username=self.SNOWFLAKE_USER,
            password=self.SNOWFLAKE_PASSWORD,
            host=self.SNOWFLAKE_ACCOUNT,
            database=f"{self.SNOWFLAKE_DATABASE}/{self.SNOWFLAKE_SCHEMA}",
            query={
                "warehouse": self.SNOWFLAKE_WAREHOUSE,
            },
        )

settings = Settings()
