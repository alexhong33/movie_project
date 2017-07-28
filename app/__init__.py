# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:16
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : __init__.py.py
# @Description : STOP wishing START doing. 

from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')
 