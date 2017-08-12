# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:17
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : forms.py
# @Description : STOP wishing START doing. 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin

class LoginForm(FlaskForm):
    # 管理员登录表单
    account = StringField(
        # 标签
        label="账号",
        # 验证器
        validators=[
            DataRequired("请输入账号!")
        ],
        # 描述
        description="账号",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            #"required": "required"
        }
    )

    pwd = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired("请输入密码!")
        ],
        # 描述
        description="密码",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            #"required": "required"
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在!")
