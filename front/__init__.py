# coding:utf-8
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'front.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # 注册蓝图
    from front.views import front # 位置不要放上面 如果你的view界面展示也在`__init__`下面, 那就把view展示相关的代码移到最下面，因为python先执行view.py相关界面，而此时db还没有创建，就会报这个错误
    app.register_blueprint(front)

    from server.views import server
    app.register_blueprint(server)

    # 注册db
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pig:xiaobing123@117.48.202.102:3310/cleanblog'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/cleanblog'
    db.init_app(app)

    # 国际化
    from flask_babelex import Babel
    babel = Babel(app)

    # # 注册flask-admin
    # admin = Admin(app, name="xiaoblog", template_mode='bootstrap3', base_template='admin/mybase.html')
    # from .models import User, Tag, Article
    # from flask_admin.contrib.sqla import ModelView
    # from front.modelview import UModelview, BaseMView, ArticleVModel
    #
    # admin.add_view(UModelview(User, db.session, name="用户管理"))
    # admin.add_view(BaseMView(Tag, db.session, category='Models', name="标签管理"))
    # admin.add_view(ArticleVModel(Article, db.session, category='Models', name="文章管理"))

    # 整合flask-login
    login_manager.init_app(app)

    return app
