from flask import redirect, url_for
from flask.views import MethodView
from werkzeug.wrappers.response import Response

from cross_stitch_tasks.api.app import crud


class DeleteJobsView(MethodView):
    def get(self, id: int) -> Response:
        # сначала нужно удалить процесс, потом саму работу
        crud.delete(table_name="processes", id=id)
        crud.delete(table_name="jobs", id=id)
        return redirect(url_for("job_list"), code=302)
