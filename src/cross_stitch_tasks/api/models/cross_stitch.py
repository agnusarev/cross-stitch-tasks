from sqlalchemy import Column, INTEGER

from cross_stitch_tasks.api.models.base_model import BaseModel


class Processes(BaseModel):
    __tablename__ = "processes"
    id = Column(INTEGER(), primary_key=True, comment="Идентификатор процесса")
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
    type_of_base = Column(INTEGER(), nullable=False, comment="Вид основы")
    type_of_image = Column(INTEGER(), nullable=False, comment="Тип изображения")
