
from flask import request
from app.models import UserLog
from app import db
from flask_appbuilder.api import expose, BaseApi
from flask_jwt_extended import jwt_required

class UserLogApi(BaseApi):
    resource_name = "userlog"

    @expose('/query', methods=["POST"])
    @jwt_required()
    def query_logs(self):
        data = request.json or {}
        username = data.get("username")
        action = data.get("action")
        page = int(data.get("page", 1))
        page_size = int(data.get("page_size", 20))

        query = db.session.query(UserLog)
        if username:
            query = query.filter(UserLog.username == username)
        if action:
            query = query.filter(UserLog.action == action)
        total = query.count()
        logs = query.order_by(UserLog.log_time.desc()).offset((page-1)*page_size).limit(page_size).all()

        result = [
            {
                "id": log.id,
                "username": log.username,
                "action": log.action,
                "ip": log.ip,
                "log_time": log.log_time.strftime('%Y-%m-%d %H:%M:%S')
            }
            for log in logs
        ]
        return self.response(200, result={
            "code": 200,
            "data": {
                "total": total,
                "logs": result
            },
            "message": "查询成功"
        })