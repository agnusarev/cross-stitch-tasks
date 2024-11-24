from typing import Any

from flask import render_template, request
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from cross_stitch_tasks.api.app import db
from cross_stitch_tasks.api.models import TypeOfImage


class TypeOfImageForm(FlaskForm):
    type = StringField("Добавить новый тип изображения", validators=[DataRequired()])


class TypeOfImageView(MethodView):
    def get(self) -> Any:
        form = TypeOfImageForm()

        return render_template("image_form.html", title="Добавить тип изображения", form=form)

    def post(self) -> Any:
        _type = request.form.get("type")
        db.session.add(TypeOfImage(type_of_image=_type))
        db.session.commit()
        return render_template("base.html", title="Home")
