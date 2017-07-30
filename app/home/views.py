# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:17
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : views.py
# @Description : STOP wishing START doing. 

from . import home
from flask import render_template

@home.route("/")
def index():
    return render_template("home/index.html")
 