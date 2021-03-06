# -*- coding: utf-8 -*-
# @Time        : 2017/7/28 17:17
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : forms.py
# @Description : STOP wishing START doing. 

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, ValidationError
from app.models import User


class RegistForm(FlaskForm):
    # 登录表单
    name = StringField(
        # 标签
        label="昵称",
        # 验证器
        validators=[
            DataRequired("请输入昵称!")
        ],
        # 描述
        description="昵称",
        # 附加选项
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称！",
        }
    )

    email = StringField(
        # 标签
        label="邮箱",
        # 验证器
        validators=[
            DataRequired("请输入邮箱!"),
            Email("邮箱格式不正确!")
        ],
        # 描述
        description="邮箱",
        # 附加选项
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱！",
        }
    )

    phone = StringField(
        # 标签
        label="手机",
        # 验证器
        validators=[
            DataRequired("请输入手机!"),
            Regexp("1[3458]\\d{9}", message="手机格式不正确!")
        ],
        # 描述
        description="手机",
        # 附加选项
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入手机！",
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
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )

    repwd = PasswordField(
        # 标签
        label="确认密码",
        # 验证器
        validators=[
            DataRequired("请输入确认密码!"),
            EqualTo('pwd', message="两次密码不一致!")
        ],
        # 描述
        description="确认密码",
        # 附加选项
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入确认密码！",
        }
    )
    submit = SubmitField(
        '注册',
        render_kw={
            "class": "btn btn-lg btn-success btn-block",
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("昵称已经存在!")

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user == 1:
            raise ValidationError("邮箱已经存在!")

    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user == 1:
            raise ValidationError("手机号码已经存在!")


class LoginForm(FlaskForm):
    name = StringField(
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
            "class": "form-control input-lg",
            "placeholder": "请输入账号！",
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
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )

    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        }
    )


class UserdetailForm(FlaskForm):
    name = StringField(
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
        }
    )

    email = StringField(
        # 标签
        label="邮箱",
        # 验证器
        validators=[
            DataRequired("请输入邮箱!"),
            Email("邮箱格式不正确!")
        ],
        # 描述
        description="邮箱",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
        }
    )

    phone = StringField(
        # 标签
        label="手机",
        # 验证器
        validators=[
            DataRequired("请输入手机!"),
            Regexp("1[3458]\\d{9}", message="手机格式不正确!")
        ],
        # 描述
        description="手机",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机！",
        }
    )

    face = FileField(
        label="头像",
        validators=[
            DataRequired("请上传头像!")
        ],
        description="头像",
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
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success",
        }
    )


class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        # 标签
        label="旧密码",
        # 验证器
        validators=[
            DataRequired("请输入旧密码!")
        ],
        # 描述
        description="旧密码",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码！",
            # "required": "required"
        }
    )
    new_pwd = PasswordField(
        # 标签
        label="新密码",
        # 验证器
        validators=[
            DataRequired("请输入新密码!")
        ],
        # 描述
        description="新密码",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码！",
            # "required": "required"
        }
    )
    submit = SubmitField(
        '修改密码',
        render_kw={
            "class": "btn btn-success",
        }
    )


class CommentForm(FlaskForm):
    content = TextAreaField(
        label="内容",
        validators=[
            DataRequired("请输入内容!"),
        ],
        description="内容",
        render_kw={
            "id": "input_content"
        }
    )

    submit = SubmitField(
        '提交评论',
        render_kw={
            "class": "btn btn-success",
            "id": "btn btn-sub"
        }
    )
