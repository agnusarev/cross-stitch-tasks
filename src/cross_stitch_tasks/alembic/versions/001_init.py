"""init

Revision ID: 001
Revises:
Create Date: 2024-12-07 14:11:20.678570

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

from cross_stitch_tasks.settings import Settings

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "types_of_base",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False, comment="Идентификатор вида основы"),
        sa.Column("type_of_base", sa.VARCHAR(length=100), nullable=False, comment="Тип основы"),
        sa.Column("time_stamp", postgresql.TIMESTAMP(timezone=True), nullable=False, comment="Момент записи данных"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        schema=Settings.DB_SCHEMA,
    )
    op.create_table(
        "types_of_image",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False, comment="Идентификатор типа изображения"),
        sa.Column("type_of_image", sa.VARCHAR(length=100), nullable=False, comment="Тип изображения"),
        sa.Column("time_stamp", postgresql.TIMESTAMP(timezone=True), nullable=False, comment="Момент записи данных"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        schema=Settings.DB_SCHEMA,
    )
    op.create_table(
        "jobs",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False, comment="Идентификатор работы"),
        sa.Column("name", sa.VARCHAR(length=200), nullable=False, comment="Название работы"),
        sa.Column("length_in_cm", sa.INTEGER(), nullable=False, comment="Длина работы в сантиметрах"),
        sa.Column("width_in_cm", sa.INTEGER(), nullable=False, comment="Ширина работы в сантиметрах"),
        sa.Column("length_in_crosses", sa.INTEGER(), nullable=False, comment="Длина работы в крестиках"),
        sa.Column("width_in_crosses", sa.INTEGER(), nullable=False, comment="Ширина работы в крестиках"),
        sa.Column("number_of_crosses", sa.INTEGER(), nullable=False, comment="Количество только крестиков"),
        sa.Column("number_of_half_crosses", sa.INTEGER(), nullable=False, comment="Количество полукрестиков"),
        sa.Column("number_of_backstitch", sa.INTEGER(), nullable=False, comment="Количество бэкстича"),
        sa.Column("number_of_remaining_stitches", sa.INTEGER(), nullable=False, comment="Количество остальных стежков"),
        sa.Column("number_of_colors", sa.INTEGER(), nullable=False, comment="Количество цветов в работе"),
        sa.Column("number_of_blends", sa.INTEGER(), nullable=False, comment="Количество блендов в работе"),
        sa.Column("is_active", sa.BOOLEAN(), nullable=False, comment="Флаг активности работы"),
        sa.Column("type_of_base_id", sa.INTEGER(), nullable=False, comment="Вид основы"),
        sa.Column("type_of_image_id", sa.INTEGER(), nullable=False, comment="Тип изображения"),
        sa.Column("time_stamp", postgresql.TIMESTAMP(timezone=True), nullable=False, comment="Момент записи данных"),
        sa.ForeignKeyConstraint(
            ["type_of_base_id"],
            [f"{Settings.DB_SCHEMA}.types_of_base.id"],
        ),
        sa.ForeignKeyConstraint(
            ["type_of_image_id"],
            [f"{Settings.DB_SCHEMA}.types_of_image.id"],
        ),
        sa.PrimaryKeyConstraint("id", "type_of_base_id", "type_of_image_id"),
        sa.UniqueConstraint("id"),
        schema=Settings.DB_SCHEMA,
    )
    op.create_table(
        "processes",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False, comment="Идентификатор процесса"),
        sa.Column("job_id", sa.INTEGER(), nullable=False, comment="Идентификатор работы"),
        sa.Column("number_of_crosses", sa.INTEGER(), nullable=True, comment="Текущее количество вышитых крестиков"),
        sa.Column(
            "number_of_half_crosses", sa.INTEGER(), nullable=True, comment="Текущее количество вышитых полукрестиков"
        ),
        sa.Column("number_of_backstitch", sa.INTEGER(), nullable=True, comment="Текущее количество вышитого бэкстича"),
        sa.Column(
            "number_of_remaining_stitches",
            sa.INTEGER(),
            nullable=True,
            comment="Текущее количество вышитых остальных стежков",
        ),
        sa.Column("is_active", sa.BOOLEAN(), nullable=False, comment="Флаг активности процесса"),
        sa.Column("time_stamp", postgresql.TIMESTAMP(timezone=True), nullable=False, comment="Момент записи данных"),
        sa.ForeignKeyConstraint(
            ["job_id"],
            [f"{Settings.DB_SCHEMA}.jobs.id"],
        ),
        sa.PrimaryKeyConstraint("id", "job_id"),
        sa.UniqueConstraint("id"),
        schema=Settings.DB_SCHEMA,
    )


def downgrade() -> None:
    op.drop_table("processes", schema=Settings.DB_SCHEMA)
    op.drop_table("jobs", schema=Settings.DB_SCHEMA)
    op.drop_table("types_of_image", schema=Settings.DB_SCHEMA)
    op.drop_table("types_of_base", schema=Settings.DB_SCHEMA)
