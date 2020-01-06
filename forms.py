from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from models import Admin


class LoginForm(FlaskForm):
    """ 登录表单 """
    # 登录账号
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号",
            # 当使用了DaraRequired()的时候,默认要求此字段必填.所以这里必须将required设置为False
            # 才能在input标签中不添加required属性
            "required": False
        }
    )
    # 登录密码
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码",
            "required": False
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class": ""
        }
    )

    def validate_account(self, field):
        # 获取当前表单中的数据
        account = field.data
        # admin表中查询出用户名为当前表单用户名的数据的条数。
        # 如果条数为0，则表示数据库中没有该用户名，则抛出验证错误ValidationError对象
        admin = Admin.query.filter_by(user=account).count()
        if admin == 0:
            raise ValidationError("账号不存在！")
