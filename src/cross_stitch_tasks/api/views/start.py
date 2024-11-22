from flask.views import MethodView

class StartApp(MethodView):

    def get(self) -> str:
        return "Hello, World!"
