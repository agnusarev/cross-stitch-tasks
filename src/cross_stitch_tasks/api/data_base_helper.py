from typing import Optional

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

# from cross_stitch_tasks.api.models import TypeOfBase


class DataBaseHelper:
    """Класс, реализующий различные операции с базой данных"""

    def __init__(self, sqlalchemy_db: "SQLAlchemy") -> None:
        self.db = sqlalchemy_db
        self.engine: Optional[Engine] = None

    def create_db_engine(self, flask_app: "Flask") -> None:
        """
        Метод для создания объекта SQLAlchemy Engine, используя параметры приложения Flask.
        """

        self.db.init_app(flask_app)

        engine_options = flask_app.config.get("SQLALCHEMY_ENGINE_OPTIONS", dict())
        self.engine = create_engine(self.db.engine.url, **engine_options)
