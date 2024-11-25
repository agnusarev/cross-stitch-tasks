from flask import render_template, request
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.validators import DataRequired

from cross_stitch_tasks.api.app import crud


class JobsForm(FlaskForm):
    length_in_cm = IntegerField("Длина работы в сантиметрах", validators=[DataRequired()])
    width_in_cm = IntegerField("Ширина работы в сантиметрах", validators=[DataRequired()])
    length_in_crosses = IntegerField("Длина работы в крестиках", validators=[DataRequired()])
    width_in_crosses = IntegerField("Ширина работы в крестиках", validators=[DataRequired()])
    number_of_crosses = IntegerField("Количество только крестиков", validators=[DataRequired()])
    number_of_half_crosses = IntegerField("Количество полукрестиков", validators=[DataRequired()])
    number_of_backstitch = IntegerField("Количество бэкстича", validators=[DataRequired()])
    number_of_remaining_stitches = IntegerField("Количество остальных стежков", validators=[DataRequired()])
    number_of_colors = IntegerField("Количество цветов в работе", validators=[DataRequired()])
    number_of_blends = IntegerField("Количество блендов в работе", validators=[DataRequired()])
    type_of_base_id = SelectField("Вид основы")
    type_of_image_id = SelectField("Тип изображения")


class JobView(MethodView):
    def get(self) -> str:
        form = JobsForm()

        _types_of_base = crud.get_actual_table("types_of_base")
        form.type_of_base_id.choices = [
            (_type["id"], _type["type_of_base"]) for _type in _types_of_base.to_dict("records")
        ]

        _type_of_image = crud.get_actual_table("types_of_image")
        form.type_of_image_id.choices = [
            (_type["id"], _type["type_of_image"]) for _type in _type_of_image.to_dict("records")
        ]

        return render_template("jobs_form.html", title="Добавить работу", form=form)

    def post(self) -> str:
        params = dict()
        params = request.form.to_dict()
        params.pop("csrf_token", None)
        params["is_active"] = True  # type: ignore
        crud.insert(table_name="jobs", params=params)
        return render_template("base.html", title="Home")
