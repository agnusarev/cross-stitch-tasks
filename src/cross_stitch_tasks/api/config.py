import os

from cross_stitch_tasks.settings import Settings


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        f"{Settings.DIALECT}+{Settings.DRIVER}://{Settings.DB_USER}"
        f":{Settings.DB_PASSWORD}@{Settings.DB_HOST}:{Settings.DB_PORT}/{Settings.DB_NAME}"
    )
    SQLALCHEMY_ENGINE_OPTIONS = {
        "echo": False,
        "pool_pre_ping": True,
        "connect_args": {"options": f"-c timezone=utc -csearch_path={Settings.DB_SCHEMA}"},
    }
