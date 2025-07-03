from flask_appbuilder.api import BaseApi, expose
from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import UserLog
from datetime import datetime
from app import db

from app.models import UserLog
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import expose, ModelRestApi

# class UserLogApi(ModelRestApi):
#     resource_name = "userlog"
#     datamodel = SQLAInterface(UserLog)

class AuthApi(BaseApi):
    resource_name = "auth"

    @expose('/login', methods=["POST"])
    def login(self):
        data = request.json or {}
        username = data.get("username")
        password = data.get("password")
        ip = request.remote_addr
        if not username or not password:
            db.session.add(UserLog(username=username or '', action='login_fail', ip=ip, log_time=datetime.utcnow()))
            db.session.commit()
            return self.response_400(message="用户名和密码不能为空")
        user = self.appbuilder.sm.find_user(username=username)
        if not user or not self.appbuilder.sm.auth_user_db(username, password):
            db.session.add(UserLog(username=username, action='login_fail', ip=ip, log_time=datetime.utcnow()))
            db.session.commit()
            return self.response_401(message="用户名或密码错误")
        access_token = create_access_token(identity=str(user.id))
        db.session.add(UserLog(username=username, action='login', ip=ip, log_time=datetime.utcnow()))
        db.session.commit()
        return self.response(200, result={
            "code": 200,
            "data": {"access_token": access_token},
            "message": "登入成功"
        })

    @expose('/logout', methods=["POST"])
    @jwt_required()
    def logout(self):
        user_id = get_jwt_identity()
        # 如果你有 user_id 到用户名的映射，可以查出用户名
        user = self.appbuilder.sm.get_user_by_id(int(user_id))
        username = user.username if user else ''
        ip = request.remote_addr
        db.session.add(UserLog(username=username, action='logout', ip=ip, log_time=datetime.utcnow()))
        db.session.commit()
        return self.response(200, message="Logout success")