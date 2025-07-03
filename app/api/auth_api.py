from flask_appbuilder.api import BaseApi, expose
from flask import request
from flask_jwt_extended import create_access_token

class AuthApi(BaseApi):
    resource_name = "auth"

    @expose('/login', methods=["POST"])
    def login(self):
        data = request.json or {}
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return self.response_400(message="用户名和密码不能为空")
        # 校验用户
        user = self.appbuilder.sm.find_user(username=username)
        if not user or not self.appbuilder.sm.auth_user_db(username, password):
            return self.response_401(message="用户名或密码错误")
        # 生成token
        access_token = create_access_token(identity=user.id)
        return self.response(200, result={
            "code": 200,
            "data": {"access_token": access_token},
            "message": "登入成功"
        })

    @expose('/logout', methods=["POST"])
    def logout(self):
        return self.response(200, message="Logout success")