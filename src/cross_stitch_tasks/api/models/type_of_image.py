from sqlalchemy import INTEGER, VARCHAR, Column
from sqlalchemy.orm import relationship

from cross_stitch_tasks.api.models.base_model import BaseModel


class TypeOfImage(BaseModel):
    __tablename__ = "types_of_image"
    id = Column(INTEGER(), primary_key=True, autoincrement=True, unique=True, comment="Идентификатор типа изображения")
    type_of_image = Column(VARCHAR(100), nullable=False, comment="Тип изображения")

    job = relationship("Jobs", back_populates="type_of_image")
