from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from cross_stitch_tasks.api.config import Config
from cross_stitch_tasks.api.data_base_helper import DataBaseHelper

db = SQLAlchemy()
crud = DataBaseHelper(sqlalchemy_db=db)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False
    from cross_stitch_tasks.api.views.urls import urls

    with app.app_context():
        crud.create_db_engine(flask_app=app)
        for resource, url, name in urls:
            app.add_url_rule(url, name, resource)

    return app
