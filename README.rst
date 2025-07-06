Flask-AppBuilder 用户认证与设备管理系统
=====================================

这是一个基于 Flask-AppBuilder 框架构建的 Web 应用，提供用户认证、设备管理和操作日志记录等功能。

功能特性
--------

🔐 **用户认证系统**
- 用户登录/登出
- JWT 令牌认证
- 登录失败记录
- IP 地址追踪

📱 **设备管理**
- 设备状态上报
- 设备监控
- 状态记录

📊 **日志系统**
- 用户操作日志记录
- 日志查询和筛选
- 分页显示
- 按时间排序

🌐 **其他特性**
- 跨域支持 (CORS)
- 国际化支持
- RESTful API 设计
- Swagger UI 支持

技术栈
------

- **Flask-AppBuilder**: 主框架，提供管理界面和 API 基础
- **Flask-JWT-Extended**: JWT 令牌认证
- **Flask-CORS**: 跨域请求支持
- **Flask-Migrate**: 数据库迁移
- **SQLAlchemy**: ORM 数据库操作

安装和运行
----------

1. **克隆项目**::

    git clone https://github.com/QiuWenLL/useFlaskDemo.git
    cd useFlaskDemo

2. **安装依赖**::

    pip install -r requirements.txt

3. **配置数据库**::

    # 复制配置文件模板
    cp config.py.tpl config.py
    
    # 编辑 config.py 配置数据库连接等信息

4. **初始化数据库**::

    python init_db.py

5. **创建管理员用户**::

    export FLASK_APP=app
    flask fab create-admin

6. **启动应用**::

    python run.py
    
    # 或者使用 Flask 命令
    flask run

应用将在 http://localhost:8080 启动

API 接口文档
------------

认证接口
~~~~~~~~

**登录**
- **URL**: ``POST /api/v1/auth/login``
- **参数**::

    {
        "username": "用户名",
        "password": "密码"
    }

- **返回**::

    {
        "code": 200,
        "data": {
            "access_token": "JWT令牌"
        },
        "message": "登入成功"
    }

**登出**
- **URL**: ``POST /api/v1/auth/logout``
- **Headers**: ``Authorization: Bearer <JWT令牌>``

设备管理接口
~~~~~~~~~~~~

**设备状态上报**
- **URL**: ``POST /api/v1/device/status``
- **Headers**: ``Authorization: Bearer <JWT令牌>``
- **参数**::

    {
        "device_id": "设备ID",
        "status": "设备状态"
    }

日志查询接口
~~~~~~~~~~~~

**查询用户日志**
- **URL**: ``POST /api/v1/userlog/query``
- **Headers**: ``Authorization: Bearer <JWT令牌>``
- **参数**::

    {
        "username": "用户名（可选）",
        "action": "操作类型（可选）",
        "page": 1,
        "page_size": 20
    }

测试接口
~~~~~~~~

**Hello World**
- **URL**: ``GET /api/v1/hello/say``
- **返回**: ``{"message": "Hello, world!"}``

项目结构
--------

::

    useFlaskDemo/
    ├── app/                    # 应用主目录
    │   ├── __init__.py        # 应用初始化
    │   ├── models.py          # 数据模型
    │   ├── views.py           # 视图
    │   ├── api/               # API 接口
    │   │   ├── auth_api.py    # 认证 API
    │   │   ├── device_api.py  # 设备管理 API
    │   │   ├── hello_api.py   # 测试 API
    │   │   └── user_log_api.py # 日志查询 API
    │   ├── templates/         # 模板文件
    │   └── translations/      # 国际化文件
    ├── babel/                 # 国际化配置
    ├── config.py              # 配置文件
    ├── config.py.tpl          # 配置文件模板
    ├── init_db.py             # 数据库初始化
    ├── run.py                 # 启动文件
    ├── requirements.txt       # 依赖包
    └── README.rst             # 项目说明

数据模型
--------

**UserLog (用户日志)**
- ``id``: 主键
- ``username``: 用户名
- ``action``: 操作类型 (login/logout/login_fail)
- ``ip``: 用户 IP 地址
- ``log_time``: 操作时间

开发指南
--------

添加新的 API
~~~~~~~~~~~~

1. 在 ``app/api/`` 目录下创建新的 API 文件
2. 继承 ``BaseApi`` 类
3. 在 ``app/__init__.py`` 中注册新的 API

数据库迁移
~~~~~~~~~~

::

    # 生成迁移文件
    flask db migrate -m "描述信息"
    
    # 执行迁移
    flask db upgrade

配置说明
--------

主要配置项在 ``config.py`` 中：

- ``SECRET_KEY``: 应用密钥
- ``SQLALCHEMY_DATABASE_URI``: 数据库连接字符串
- ``JWT_SECRET_KEY``: JWT 密钥
- ``LANGUAGES``: 支持的语言

许可证
------

MIT License

贡献
----

欢迎提交 Issue 和 Pull Request！

联系方式
--------

- GitHub: https://github.com/QiuWenLL/useFlaskDemo
