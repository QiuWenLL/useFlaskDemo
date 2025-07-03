from flask_appbuilder.api import BaseApi, expose

class AuthApi(BaseApi):
    resource_name = "auth"

    @expose('/logout', methods=["POST"])
    def logout(self):
        # 这里可以做token黑名单等操作，简单场景直接返回成功
        return self.response(200, message="Logout success")