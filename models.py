# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mysql@sleeptoroll.xyz:3306/db_cma_test"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# db = SQLAlchemy(app)

from exts import db


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    pwd = db.Column(db.String(128), nullable=False)

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        # 验证hash密码
        # 如果模型中的pwd和传入的pwd一致，则返回true
        return check_password_hash(self.pwd, pwd)


# if __name__ == "__main__":
#     # 导入生成hash密码加密的工具
#     from werkzeug.security import generate_password_hash
#     admin = Admin(
#         user="acc2",
#         pwd=generate_password_hash("acc2")  # 使用密码工具给密码加密
#     )
#     db.session.add(admin)
#     db.session.commit()
