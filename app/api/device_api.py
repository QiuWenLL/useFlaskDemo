from flask_appbuilder.api import BaseApi, expose
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request

class DeviceApi(BaseApi):
    resource_name = "device"
    allow_browser_login = True  # 允许前端调试用 Swagger UI

    @expose('/status', methods=["POST"])
    @jwt_required()
    def report_status(self):
        identity = get_jwt_identity()
        data = request.json or {}

        device_id = data.get("device_id")
        status = data.get("status")

        if not device_id or not status:
            return self.response_400(message="device_id and status are required")

        # 这里你可以将数据存入数据库或其他业务逻辑
        print(f"用户 [{identity}] 上报设备 {device_id} 状态：{status}")

        return self.response(200, message="Status received")

