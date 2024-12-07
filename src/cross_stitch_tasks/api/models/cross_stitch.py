from sqlalchemy import BOOLEAN, INTEGER, VARCHAR, Column, ForeignKey
from sqlalchemy.orm import relationship

from cross_stitch_tasks.api.models.base_model import BaseModel

# from cross_stitch_tasks.env_vars import DB_SCHEMA


# class Users(BaseModel):
#     __tablename__ = "users"
#     id = Column(INTEGER(), primary_key=True, autoincrement=True, comment="Идентификатор пользователя")
#     email = Column(VARCHAR(100), comment="Email пользователя")


class TypeOfBase(BaseModel):
    __tablename__ = "types_of_base"
    id = Column(INTEGER(), primary_key=True, autoincrement=True, unique=True, comment="Идентификатор вида основы")
    type_of_base = Column(VARCHAR(100), nullable=False, comment="Тип основы")

    job = relationship("Jobs", back_populates="type_of_base")


class TypeOfImage(BaseModel):
    __tablename__ = "types_of_image"
    id = Column(INTEGER(), primary_key=True, autoincrement=True, unique=True, comment="Идентификатор типа изображения")
    type_of_image = Column(VARCHAR(100), nullable=False, comment="Тип изображения")

    job = relationship("Jobs", back_populates="type_of_image")


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
