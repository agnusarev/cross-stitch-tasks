from flask import redirect, render_template, request, url_for
from flask.views import MethodView
from flask_wtf import FlaskForm
from werkzeug.wrappers.response import Response
from wtforms import StringField
from wtforms.validators import DataRequired

from cross_stitch_tasks.api.app import crud


class TypeOfBaseForm(FlaskForm):
    type = StringField("Добавить новый тип основы", validators=[DataRequired()])


class TypeOfBaseView(MethodView):
    def get(self) -> str:
        form = TypeOfBaseForm()

        return render_template("type_form.html", title="Добавить тип основы", form=form)

    def post(self) -> Response:
        params = dict()
        params["type_of_base"] = request.form.get("type")
        crud.insert(table_name="types_of_base", params=params)
        return redirect(url_for("types_list"), code=302)


class TypeOfBase(MethodView):
    def get(self) -> str:
        types = crud.get_actual_table("types_of_base").to_dict("records")

        return render_template("type_list.html", title="Список тип основы", types=types)
