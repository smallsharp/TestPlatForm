import os
from datetime import timedelta

# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'dbdev'
PASSWORD = '123456'
HOST = '192.168.40.67'
PORT = '3306'
DATABASE = 'test'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(24)

# 设置session过期时间
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
