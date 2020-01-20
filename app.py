from flask import Flask, render_template, request, flash, session, redirect, flash, url_for, flash
from exts import db
import config
from models import Admin
from forms import LoginForm, RegisterForm
from functools import wraps
from werkzeug.security import generate_password_hash

app = Flask(__name__, static_url_path='')
app.config.from_object(config)
db.init_app(app)

app.config['SECRET_KEY'] = '213a4sdfrafds@#rgt'


# 用户登录访问控制装饰器
def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin(
            username=data["account"],
            pwd=generate_password_hash(data["pwd"]),  # hash加密密码
            email=data["email"],
            create_time=data["create_time"]
        )
        db.session.add(admin)
        db.session.commit()
        flash("注册成功，请登录！", "reg_ok")
        return redirect(url_for("login"))
    return render_template('register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        # 验证用户名(validate_account())和密码(check_pwd())
        admin = Admin.query.filter_by(
            username=data["account"]).first()  # 数据库中查询出当前表单中传入的用户名对应的一条记录
        # 如果对应的密码不正确则闪现提示,并重定向到登录页面
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！")
            return redirect(url_for("login"))

        # 如果正确则定义session保存用户
        session["admin"] = data["account"]
        # 并跳转到next或者登录后的首页仪表盘页面
        return redirect(request.args.get("next") or url_for("index"))
    return render_template('login.html', form=form)


@app.route('/logout')
@admin_login_req
def logout():
    # 删除session中当前用户account
    session.pop("admin", None)
    flash("退出成功，请重新登录！")
    return redirect(url_for("login"))


@app.route('/user')
@admin_login_req
def index():
    name = session.get('admin')  # 或者使用字典的用法获取键的值 name = session['admin']
    return render_template("index.html", username=name)


@app.route('/user_list')
@admin_login_req
def user_list():
    name = session.get('admin')
    users = db.session.query(Admin).all()
    return render_template("user_list.html", username=name, users=users)


if __name__ == '__main__':
    app.run(debug=True)
