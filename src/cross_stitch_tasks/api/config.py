import os

from cross_stitch_tasks.env_vars import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_SCHEMA, DB_USER, DIALECT, DRIVER


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"{DIALECT}+{DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "echo": False,
        "connect_args": {"options": f"-c timezone=utc -csearch_path={DB_SCHEMA}"},
    }
