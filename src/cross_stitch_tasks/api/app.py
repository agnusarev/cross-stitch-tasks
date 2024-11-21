from flask_sqlalchemy import SQLAlchemy

from cross_stitch_tasks.api.data_base_helper import DataBaseHelper

db = SQLAlchemy()
crud = DataBaseHelper(sqlalchemy_db=db)
