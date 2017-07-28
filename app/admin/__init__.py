# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:17
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : __init__.py.py
# @Description : STOP wishing START doing. 

from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views
 