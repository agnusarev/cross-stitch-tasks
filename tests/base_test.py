import logging
import os
import time
from typing import Any, Never, TYPE_CHECKING

import pytest
from dotenv import load_dotenv
from flask_migrate import Migrate, upgrade
from sqlalchemy import text

load_dotenv()

LOGGER = logging.getLogger(__name__)

HEALTHCHECK_TRIES = 10


class BaseTest:
    test_db_name = os.getenv("TEST_DB_NAME")
    test_db_user = os.getenv("TEST_DB_USER")
    test_db_password = os.getenv("TEST_DB_PASSWORD")
    test_db_host = os.getenv("TEST_DB_HOST")
    test_db_port = os.getenv("TEST_DB_PORT")
    test_db_schema = os.getenv("TEST_DB_SCHEMA")
    test_dialect = os.getenv("TEST_DIALECT")
    test_driver = os.getenv("TEST_DRIVER")
    test_secret_key = os.getenv("TEST_SECRET_KEY")
    sqlalchemy_database_uri = (
        f"{test_dialect}+{test_driver}://"
        f"{test_db_user}:{test_db_password}@"
        f"{test_db_host}:{test_db_port}/"
        f"{test_db_name}"
    )

    @pytest.fixture(scope="session")
    def db_healthcheck(self) -> None:
        """Фикстура для проверки готовности базы данных."""
        import psycopg2

        for i in range(HEALTHCHECK_TRIES):
            try:
                connection = psycopg2.connect(
                    dbname=self.test_db_name,
                    user=self.test_db_user,
                    password=self.test_db_password,
                    host=self.test_db_host,
                    port=self.test_db_port,
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

        Config.SQLALCHEMY_DATABASE_URI = self.sqlalchemy_database_uri
        Config.SQLALCHEMY_ENGINE_OPTIONS["connect_args"] = {
            "options": f"-c timezone=utc -csearch_path={self.test_db_schema}"
        }

    @pytest.fixture(scope="class")
    def app(self, define_params: Never, db_healthcheck: Never) -> Any:
        """
        Фикстура для создания инстанса приложения Flask и настройки переменных.
        """
        if TYPE_CHECKING:
            print(define_params)
            print(db_healthcheck)
        from cross_stitch_tasks.api.app import create_app

        test_config = {
            "TESTING": True,
            "DB_SCHEMA": self.test_db_schema,
            "SQLALCHEMY_DATABASE_URI": self.sqlalchemy_database_uri,
            "SECRET_KEY": self.test_secret_key,
        }
        app = create_app(test_config)
        with app.app_context():
            yield app

    @pytest.fixture(scope="class")
    def crud(self, app: Any) -> Any:
        """
        Метод для подключения к тестовой базе данных.
        """
        from cross_stitch_tasks.env_vars import ROOT_FOLDER
        from cross_stitch_tasks.api.app import crud

        with crud.db.engine.connect() as conn:
            conn.execute(text(f"DROP SCHEMA IF EXISTS {self.test_db_schema} CASCADE;"))
            conn.commit()
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {self.test_db_schema};"))
            conn.commit()

        crud.schema = self.test_db_schema
        Migrate(app, crud.db, ROOT_FOLDER / "src" / "cross_stitch_tasks" / "alembic")
        upgrade(revision="head")

        yield crud

        with crud.db.engine.connect() as conn:
            conn.execute(text(f"DROP SCHEMA IF EXISTS {self.test_db_schema} CASCADE;"))
            conn.commit()

    @pytest.fixture
    def get_client_(self, app: Any) -> Any:
        with app.test_client() as client:
            yield client
