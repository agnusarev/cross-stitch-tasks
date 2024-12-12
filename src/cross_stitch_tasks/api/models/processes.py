from sqlalchemy import BOOLEAN, INTEGER, Column, ForeignKey

from cross_stitch_tasks.api.models.base_model import BaseModel


class Processes(BaseModel):
    __tablename__ = "processes"
    id = Column(INTEGER(), primary_key=True, unique=True, autoincrement=True, comment="Идентификатор процесса")
    job_id = Column(INTEGER(), ForeignKey("jobs.id"), primary_key=True, comment="Идентификатор работы")
    number_of_crosses = Column(INTEGER(), nullable=True, default=0, comment="Текущее количество вышитых крестиков")
    number_of_half_crosses = Column(
        INTEGER(), nullable=True, default=0, comment="Текущее количество вышитых полукрестиков"
    )
    number_of_backstitch = Column(INTEGER(), nullable=True, default=0, comment="Текущее количество вышитого бэкстича")
    number_of_remaining_stitches = Column(
        INTEGER(), nullable=True, default=0, comment="Текущее количество вышитых остальных стежков"
    )
    is_active = Column(BOOLEAN(), nullable=False, default=True, comment="Флаг активности процесса")  # type: ignore
