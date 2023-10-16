from core.configs import settings
from sqlalchemy import Column, Integer, String


class ExampleModel(settings.DBBaseModel):
    __tablename__ = 'example'

    pass