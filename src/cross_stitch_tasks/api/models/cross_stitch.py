from sqlalchemy import Column, Integer, String

from cross_stitch_tasks.api.models.base_model import BaseModel


class SomeClass(BaseModel):
    __tablename__ = "some_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
