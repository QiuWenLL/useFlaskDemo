import logging
from flask import Flask
from flask_cors import CORS
from flask_appbuilder import AppBuilder, SQLA
from flask_appbuilder.api import BaseApi, expose

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app)  # 立刻加跨域支持
app.config.from_object("config")

db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

from . import views
from .api.device_api import DeviceApi
from .api.hello_api import HelloApi
appbuilder.add_api(DeviceApi)
appbuilder.add_api(HelloApi)
