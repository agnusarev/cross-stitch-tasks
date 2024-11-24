from typing import Any

from flask import render_template, request
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from cross_stitch_tasks.api.app import db
from cross_stitch_tasks.api.models import TypeOfBase


class TypeOfBaseForm(FlaskForm):
    type = StringField("Добавить новый тип основы", validators=[DataRequired()])


class TypeOfBaseView(MethodView):
    def get(self) -> Any:
        form = TypeOfBaseForm()

        return render_template("type_form.html", title="Добавить тип основы", form=form)

    def post(self) -> Any:
        _type = request.form.get("type")
        db.session.add(TypeOfBase(type_of_base=_type))
        db.session.commit()
        return render_template("base.html", title="Home")
