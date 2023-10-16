from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeBase


class Settings(BaseSettings):
    """
    General Settings API
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://USER:PASS@localhost:5432/DATABASE"
    DBBaseModel: ClassVar[DeclarativeBase] = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
