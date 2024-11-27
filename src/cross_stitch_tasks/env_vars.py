import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_SCHEMA = os.getenv("DB_SCHEMA")
DIALECT = os.getenv("DIALECT")
DRIVER = os.getenv("DRIVER")
SECRET_KEY = os.getenv("SECRET_KEY")
ROOT_FOLDER = Path(__file__).parent.parent.parent.absolute()

# TEST
TEST_DB_NAME = os.getenv("TEST_DB_NAME")
TEST_DB_USER = os.getenv("TEST_DB_USER")
TEST_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")
TEST_DB_HOST = os.getenv("TEST_DB_HOST")
TEST_DB_PORT = os.getenv("TEST_DB_PORT")
TEST_DB_SCHEMA = os.getenv("TEST_DB_SCHEMA")
TEST_DIALECT = os.getenv("TEST_DIALECT")
TEST_DRIVER = os.getenv("TEST_DRIVER")
TEST_SECRET_KEY = os.getenv("TEST_SECRET_KEY")
