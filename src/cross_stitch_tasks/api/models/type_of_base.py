from sqlalchemy import INTEGER, VARCHAR, Column
from sqlalchemy.orm import relationship

from cross_stitch_tasks.api.models.base_model import BaseModel


class TypeOfBase(BaseModel):
    __tablename__ = "types_of_base"
    id = Column(INTEGER(), primary_key=True, autoincrement=True, unique=True, comment="Идентификатор вида основы")
    type_of_base = Column(VARCHAR(100), nullable=False, comment="Тип основы")

    job = relationship("Jobs", back_populates="type_of_base")
