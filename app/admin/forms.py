# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:17
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : forms.py
# @Description : STOP wishing START doing. 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin, Tag

tags = Tag.query.all()


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
            # "required": "required"
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
            # "required": "required"
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


class TagForm(FlaskForm):
    name = StringField(
        label="名称",
        validators=[
            DataRequired("请输入标签!")
        ],
        description="标签",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入标签名称！"
        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )


class MovieForm(FlaskForm):
    title = StringField(
        label="片名",
        validators=[
            DataRequired("请输入片名!")
        ],
        description="片名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入片名！"
        }
    )
    url = FileField(
        label="文件",
        validators=[
            DataRequired("请上传文件!")
        ],
        description="文件",
    )
    info = TextAreaField(

        label="简介",
        validators=[
            DataRequired("请输入简介!")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    logo = FileField(
        label="封面",
        validators=[
            DataRequired("请上传封面!")
        ],
        description="封面",
    )
    star = SelectField(
        label="星级",
        validators=[
            DataRequired("请上传星级!")
        ],
        coerce=int,
        choices=[(1, "1星"), (2, "2星"), (3, "3星"), (4, "4星"), (5, "5星")],
        description="星级",
        render_kw={
            "class": "form-control",
        }
    )
    tag_id = SelectField(
        label="标签",
        validators=[
            DataRequired("请上传标签!")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in tags],
        description="标签",
        render_kw={
            "class": "form-control",
        }
    )
    area = StringField(
        label="地区",
        validators=[
            DataRequired("请输入地区!")
        ],
        description="地区",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入地区！"
        }
    )

    length = StringField(
        label="片长",
        validators=[
            DataRequired("请输入片长!")
        ],
        description="片长",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入片长！"
        }
    )
    release_time = StringField(
        label="上映时间",
        validators=[
            DataRequired("请输入上映时间!")
        ],
        description="上映时间",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入上映时间！",
            "id": "input_release_time"
        }
    )
    submit = SubmitField(
        '编辑',
        render_kw={
            "class": "btn btn-primary",
        }
    )
