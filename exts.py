""" exts.py是为了解决循环引用，单独把SQL-Alchemy独立出去的代码文件 """
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
