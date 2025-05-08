from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class BaseConfig(BaseModel):
    url: str = "sqlite+aiosqlite://messenger.sqlite3"
    echo: bool = True
    pool_size: int = 10
    max_overflow: int = 15


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: BaseConfig


settings = Settings()