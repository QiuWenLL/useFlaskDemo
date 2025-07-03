from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import DateTime
from datetime import datetime

class UserLog(Model):
    __tablename__ = 'user_log'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    action = Column(String(32), nullable=False)  # 如 login/logout
    ip = Column(String(64))
    log_time = Column(DateTime, default=datetime.utcnow)
