from flask.views import MethodView
from flask import render_template

class StartApp(MethodView):

    def get(self) -> str:
        user = {'username': 'Miguel'}
        return render_template('index.html', title='Home', user=user)
