from sqlalchemy import BOOLEAN, INTEGER, VARCHAR, Column, ForeignKey
from sqlalchemy.orm import relationship

from cross_stitch_tasks.api.models.base_model import BaseModel


class Jobs(BaseModel):
    __tablename__ = "jobs"
    id = Column(INTEGER(), primary_key=True, autoincrement=True, unique=True, comment="Идентификатор работы")
    name = Column(VARCHAR(200), nullable=False, comment="Название работы")
    length_in_cm = Column(INTEGER(), nullable=False, comment="Длина работы в сантиметрах")
    width_in_cm = Column(INTEGER(), nullable=False, comment="Ширина работы в сантиметрах")
    length_in_crosses = Column(INTEGER(), nullable=False, comment="Длина работы в крестиках")
    width_in_crosses = Column(INTEGER(), nullable=False, comment="Ширина работы в крестиках")
    number_of_crosses = Column(INTEGER(), nullable=False, comment="Количество только крестиков")
    number_of_half_crosses = Column(INTEGER(), nullable=False, comment="Количество полукрестиков")
    number_of_backstitch = Column(INTEGER(), nullable=False, comment="Количество бэкстича")
    number_of_remaining_stitches = Column(INTEGER(), nullable=False, comment="Количество остальных стежков")
    number_of_colors = Column(INTEGER(), nullable=False, comment="Количество цветов в работе")
    number_of_blends = Column(INTEGER(), nullable=False, comment="Количество блендов в работе")
    is_active = Column(BOOLEAN(), nullable=False, comment="Флаг активности работы")  # type: ignore

    type_of_base_id = Column(INTEGER(), ForeignKey("types_of_base.id"), primary_key=True, comment="Вид основы")
    type_of_base = relationship("TypeOfBase", back_populates="job")

    type_of_image_id = Column(INTEGER(), ForeignKey("types_of_image.id"), primary_key=True, comment="Тип изображения")
    type_of_image = relationship("TypeOfImage", back_populates="job")
