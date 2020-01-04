from flask_script import Manager
from app import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import Admin


manager = Manager(app)
# python manage.py db init/migrate -m "" /upgrade
# 模型 -> 迁移文件 -> 表
# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(app, db)

# 2.把migrateCommand命令添加到manager中。
manager.add_command('db',MigrateCommand)

if __name__ =='__main__':
    manager.run()