import os
from dataclasses import dataclass
from pathlib import Path
from typing import Union

from dotenv import load_dotenv

load_dotenv()


@dataclass
class MainSettings:
    ROOT_FOLDER: Path = Path(__file__).parent.parent.parent.absolute()


@dataclass
class Settings(MainSettings):
    DB_NAME: Union[str, None] = os.getenv("DB_NAME")
    DB_USER: Union[str, None] = os.getenv("DB_USER")
    DB_PASSWORD: Union[str, None] = os.getenv("DB_PASSWORD")
    DB_HOST: Union[str, None] = os.getenv("DB_HOST")
    DB_PORT: Union[str, None] = os.getenv("DB_PORT")
    DB_SCHEMA: Union[str, None] = os.getenv("DB_SCHEMA")
    DIALECT: Union[str, None] = os.getenv("DIALECT")
    DRIVER: Union[str, None] = os.getenv("DRIVER")
    SECRET_KEY: Union[str, None] = os.getenv("SECRET_KEY")
