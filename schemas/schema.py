from typing import Optional

from pydantic import BaseModel as SCBaseModel

class ExampleSchema(SCBaseModel):
    pass
    class Config:
        orm_mode = True

