from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from .models import UserLog
from . import appbuilder, db

class UserLogView(ModelView):
    """用户日志视图"""
    datamodel = SQLAInterface(UserLog)
    route_base = "/userlogs"
    list_columns = ['username', 'action', 'ip', 'log_time']
    show_fieldsets = [
        ('Summary', {'fields': ['username', 'action']}),
        ('Details', {'fields': ['ip', 'log_time'], 'expanded': True})
    ]

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    """
    全局404错误处理
    """
    return (
        render_template(
            "404.html", 
            base_template=appbuilder.base_template, 
            appbuilder=appbuilder
        ),
        404,
    )

# 注册视图
appbuilder.add_view(
    UserLogView,
    "用户日志",
    icon="fa-book",
    category="日志管理"
)

db.create_all()
