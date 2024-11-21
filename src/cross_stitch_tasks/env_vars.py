from dotenv import load_dotenv
from pathlib import Path
import os

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
