# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:17
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : views.py
# @Description : STOP wishing START doing. 

from . import home

@home.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"

 