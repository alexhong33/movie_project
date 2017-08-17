# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:16
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : __init__.py.py
# @Description : STOP wishing START doing. 

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
#传入数据库连接
#定义数据库连接
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

"""
获取随即密码
> import uuid
> uuid.uuid4().hex
> '4e63cc22adf245799549c36e46918681'
"""
app.config["SECRET_KEY"] = '4e63cc22adf245799549c36e46918681'
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
 