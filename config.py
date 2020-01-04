""" 数据库配置文件 """
DIALECT = 'mysql'  # 数据库--mysql
DRIVER = 'pymysql'  # 连接数据库驱动
USERNAME = 'root'  # 数据库用户名
PASSWORD = 'mysql'  # 数据库密码
HOST = 'sleeptoroll.xyz'  # 数据库所在服务器的ip或者域名
PORT = '3306'  # 端口
DATABASE = 'db_cma_test'  # 数据库名

# 格式化数据库
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True