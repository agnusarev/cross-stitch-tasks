import logging
import os
import time
from dataclasses import dataclass
from typing import Any, Union

import pytest
from dotenv import load_dotenv
from flask_migrate import Migrate, upgrade
from sqlalchemy import text

from cross_stitch_tasks.settings import MainSettings

load_dotenv()

LOGGER = logging.getLogger(__name__)

HEALTHCHECK_TRIES = 10


@dataclass
class SettingsTest(MainSettings):
    TEST_DB_NAME: Union[str, None] = os.getenv("TEST_DB_NAME")
    TEST_DB_USER: Union[str, None] = os.getenv("TEST_DB_USER")
    TEST_DB_PASSWORD: Union[str, None] = os.getenv("TEST_DB_PASSWORD")
    TEST_DB_HOST: Union[str, None] = os.getenv("TEST_DB_HOST")
    TEST_DB_PORT: Union[str, None] = os.getenv("TEST_DB_PORT")
    TEST_DB_SCHEMA: Union[str, None] = os.getenv("TEST_DB_SCHEMA")
    TEST_DIALECT: Union[str, None] = os.getenv("TEST_DIALECT")
    TEST_DRIVER: Union[str, None] = os.getenv("TEST_DRIVER")
    TEST_SECRET_KEY: Union[str, None] = os.getenv("TEST_SECRET_KEY")


class BaseTest:
    sqlalchemy_database = (
        f"{SettingsTest.TEST_DIALECT}+{SettingsTest.TEST_DRIVER}://"
        f"{SettingsTest.TEST_DB_USER}:{SettingsTest.TEST_DB_PASSWORD}@"
        f"{SettingsTest.TEST_DB_HOST}:{SettingsTest.TEST_DB_PORT}/"
        f"{SettingsTest.TEST_DB_NAME}"
    )

    @pytest.fixture(scope="session")
    def db_healthcheck(self) -> None:
        """Фикстура для проверки готовности базы данных."""
        import psycopg2

        for i in range(HEALTHCHECK_TRIES):
            try:
                connection = psycopg2.connect(
                    dbname=SettingsTest.TEST_DB_NAME,
                    user=SettingsTest.TEST_DB_USER,
                    password=SettingsTest.TEST_DB_PASSWORD,
                    host=SettingsTest.TEST_DB_HOST,
                    port=SettingsTest.TEST_DB_PORT,
                )
                cur = connection.cursor()
                cur.execute("SELECT 1;")
                cur.close()
                break
            except psycopg2.OperationalError as e:
                if i == (HEALTHCHECK_TRIES - 1):
                    LOGGER.warning(f"Last try #{i + 1} to connect to test db was unsuccessfull.")
                    pytest.exit(f"Failed to setup test database: {e}", returncode=2)
                else:
                    LOGGER.warning(f"Try #{i + 1} to connect to test db was unsuccessfull. Will try again...")
                    time.sleep(10)
                    continue

    @pytest.fixture(scope="class")
    def define_params(self) -> None:
        from cross_stitch_tasks.api.config import Config
        from cross_stitch_tasks.settings import Settings

        Config.SQLALCHEMY_DATABASE_URI = self.sqlalchemy_database
        Config.SQLALCHEMY_ENGINE_OPTIONS["connect_args"] = {
            "options": f"-c timezone=utc -csearch_path={SettingsTest.TEST_DB_SCHEMA}"
        }
        Settings.DB_SCHEMA = SettingsTest.TEST_DB_SCHEMA

    @pytest.fixture(scope="class")
    def app(self, define_params, db_healthcheck) -> Any:  # type: ignore
        """
        Фикстура для создания инстанса приложения Flask и настройки переменных.
        """
        from cross_stitch_tasks.api.app import create_app

        test_config = {
            "TESTING": True,
            "DB_SCHEMA": SettingsTest.TEST_DB_SCHEMA,
            "SQLALCHEMY_DATABASE_URI": self.sqlalchemy_database,
            "SECRET_KEY": SettingsTest.TEST_SECRET_KEY,
        }
        app = create_app(test_config)
        with app.app_context():
            yield app

    @pytest.fixture(scope="class")
    def crud(self, app: Any) -> Any:
        """
        Метод для подключения к тестовой базе данных.
        """
        from cross_stitch_tasks.api.app import crud

        with crud.db.engine.connect() as conn:
            conn.execute(text(f"DROP SCHEMA IF EXISTS {SettingsTest.TEST_DB_SCHEMA} CASCADE;"))
            conn.commit()
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SettingsTest.TEST_DB_SCHEMA};"))
            conn.commit()

        crud.schema = SettingsTest.TEST_DB_SCHEMA
        Migrate(app, crud.db, SettingsTest.ROOT_FOLDER / "src" / "cross_stitch_tasks" / "alembic")
        upgrade(revision="head")

        yield crud

        crud.db.session.close()
        crud.db.engine.dispose()
        with crud.db.engine.connect() as conn:
            conn.execute(text(f"DROP SCHEMA IF EXISTS {SettingsTest.TEST_DB_SCHEMA} CASCADE;"))
            conn.commit()

    @pytest.fixture
    def get_client_(self, app: Any) -> Any:
        with app.test_client() as client:
            yield client
