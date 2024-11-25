from functools import cached_property
from typing import TYPE_CHECKING, List, Optional, Type

import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc, insert, select
from sqlalchemy.engine.base import Engine

from cross_stitch_tasks.api.errors import ReadDBException

if TYPE_CHECKING:
    from cross_stitch_tasks.api.models.base_model import BaseModel


class DataBaseHelper:
    """Класс, реализующий различные операции с базой данных"""

    def __init__(self, sqlalchemy_db: "SQLAlchemy") -> None:
        self.db = sqlalchemy_db
        self.engine: Optional[Engine] = None

    def create_db_engine(self, flask_app: "Flask") -> None:
        """
        Метод для создания объекта SQLAlchemy Engine, используя параметры приложения Flask.
        """
        from cross_stitch_tasks.api import models  # noqa: F401

        self.db.init_app(flask_app)

        engine_options = flask_app.config.get("SQLALCHEMY_ENGINE_OPTIONS", dict())
        self.engine = create_engine(self.db.engine.url, **engine_options)

    @cached_property
    def all_models(self) -> List[Type["BaseModel"]]:
        """Свойство для получения списка всех моделей в БД.

        Returns
        -------
        List[BaseModel]
            Список моделей.
        """
        mappers = self.db.Model.registry.mappers  # type: ignore
        return [mapper.entity for mapper in mappers]

    def get_model_by_table_name(self, table_name: str) -> Type["BaseModel"]:
        """Метод для получения модели по названию таблицы.

        Parameters
        ----------
        table_name: Название таблицы.

        Returns
        -------
        BaseModel
            Объект модели.

        Raises
        ------
        ReadDBException
            Если таблица не найдена в БД.
        """
        filtered_model: List[Type["BaseModel"]] = list(
            filter(lambda model: hasattr(model, "__tablename__") and model.__tablename__ == table_name, self.all_models)
        )

        if not filtered_model:
            raise ReadDBException(f"{table_name} не найдена в БД.")

        return filtered_model[0]

    def insert(self, table_name: str, params: dict) -> None:
        """Общий метод для вставки новых записей в БД.

        Parameters
        ----------
        table_name : str
            Название таблицы, в которую будет вставка.
        params : dict
            Словарь в котором key - название поля модели, value - значение для вставки.
        """
        _model = self.get_model_by_table_name(table_name)
        stmt = insert(_model).values(**params)

        try:
            self.db.session.execute(stmt)
            self.db.session.commit()
        except exc.SQLAlchemyError:
            self.db.session.rollback()
            self.db.session.close()
            self.db.engine.dispose()
            raise
        return

    def get_actual_table(self, table_name: str) -> pd.DataFrame:
        """Общий читатель из БД, возвращает датафрейм.

        Parameters
        ----------
        table_name : str
            Имя таблицы.

        Returns
        -------
        pd.DataFrame
            Датафррейм.
        """
        _model = self.get_model_by_table_name(table_name)
        stmt = select(_model)
        df = pd.read_sql(stmt, self.db.session.connection())
        df = df.drop(columns=["time_stamp"], axis=1)
        if df.empty:
            raise ReadDBException(f"Запрашивамая таблица {table_name} пуста.")
        return df
