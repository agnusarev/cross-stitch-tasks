from flask import redirect, render_template, request, url_for
from flask.views import MethodView
from flask_wtf import FlaskForm
from werkzeug.wrappers.response import Response
from wtforms import IntegerField
from wtforms.validators import DataRequired

from cross_stitch_tasks.api.app import crud


class ProcessesForm(FlaskForm):
    number_of_crosses = IntegerField("Количество только крестиков", validators=[DataRequired()])
    number_of_half_crosses = IntegerField("Количество полукрестиков", validators=[DataRequired()])
    number_of_backstitch = IntegerField("Количество бэкстича", validators=[DataRequired()])
    number_of_remaining_stitches = IntegerField("Количество остальных стежков", validators=[DataRequired()])


class ProcessesView(MethodView):
    def get(self, id: int) -> str:
        form = ProcessesForm()

        _processes = crud.get_actual_table("processes")
        _processes = _processes.loc[_processes["id"] == id].to_dict("records")[0]

        form = ProcessesForm(
            number_of_crosses=_processes["number_of_crosses"],
            number_of_half_crosses=_processes["number_of_half_crosses"],
            number_of_backstitch=_processes["number_of_backstitch"],
            number_of_remaining_stitches=_processes["number_of_remaining_stitches"],
        )

        return render_template("processes_form.html", title="Скорректировать процесс", form=form)

    def post(self, id: int) -> Response:
        params = dict()
        params = request.form.to_dict()
        params.pop("csrf_token", None)

        crud.update(table_name="processes", id=id, params=params)

        return redirect(url_for("job_list"), code=302)
