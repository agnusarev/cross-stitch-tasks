from flask import redirect, render_template, request, url_for
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug.wrappers.response import Response

from cross_stitch_tasks.api.app import crud


class TypeOfImageForm(FlaskForm):
    type = StringField("Добавить новый тип изображения", validators=[DataRequired()])


class TypeOfImageView(MethodView):
    def get(self) -> str:
        form = TypeOfImageForm()

        return render_template("image_form.html", title="Добавить тип изображения", form=form)

    def post(self) -> Response:
        params = dict()
        params["type_of_image"] = request.form.get("type")
        crud.insert(table_name="types_of_image", params=params)
        return redirect(url_for("index"), code=201)
