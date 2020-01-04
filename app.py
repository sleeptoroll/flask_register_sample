from flask import Flask, render_template, request, flash, session, redirect, flash, url_for
from exts import db
import config
from models import Admin

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.config['SECRET_KEY'] = '213a4sdfrafds@#rgt'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form.get('user')
        pwd1 = request.form.get('pwd1')
        pwd2 = request.form.get('pwd2')
        if all([user, pwd1, pwd2]):
            if pwd1 == pwd2:
                a = Admin()
                a.user = user
                a.pwd = pwd1
                db.session.add(a)
                db.session.commit()
                flash('注册成功')
            else:
                flash('两次密码输入不一致')
        else:
            flash('输入信息不全')
    return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if all([user, pwd]):
            a = Admin.query.filter(Admin.user == user).first()
            if a:
                # 如果用户存在，判断密码是否正确
                if a.pwd == pwd:
                    # 登录成功后，session['admin_id']存入数据，
                    # 其他页面用来判断用户到登录状态
                    session['admin_id'] = a.id
                    flash('登陆成功')
                    # 登录成功后跳转到首页，对图书进行管理
                    return redirect(url_for('index'))
                else:
                    flash('密码错误')
            else:
                flash('用户名不存在')
        else:
            flash('用户名、密码不完整')
    return render_template('login.html')


@app.route('/user')
def index():
    return 'User Dashboard'


if __name__ == '__main__':
    app.run()
