# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:16
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : __init__.py.py
# @Description : STOP wishing START doing. 

from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views
