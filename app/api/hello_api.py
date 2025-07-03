from flask_appbuilder.api import BaseApi, expose

class HelloApi(BaseApi):
    resource_name = "hello"

    @expose('/say', methods=["GET"])
    def say_hello(self):
        return self.response(200, message="Hello, world!")