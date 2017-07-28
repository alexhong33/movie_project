# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:17
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : views.py
# @Description : STOP wishing START doing. 

from . import admin

@admin.route("/")

def index():
    return "<h1 style='color:red'>this is admin</h1>"

 