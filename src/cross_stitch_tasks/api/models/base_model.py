from sqlalchemy import exc

from sqlalchemy import DateTime, Column, func

from cross_stitch_tasks.api.app import db
from cross_stitch_tasks.settings import Settings


class BaseModel(db.Model):  # type: ignore
    __abstract__ = True
    base_table_args = {"schema": Settings.DB_SCHEMA}
    time_stamp = Column(DateTime(), nullable=False, default=func.now(), comment="Момент записи данных")

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        self.schema = Settings.DB_SCHEMA

    @staticmethod
    def commit_db() -> None:
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            db.session.rollback()
            raise
        finally:
            db.session.close()
            db.engine.dispose()
