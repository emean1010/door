#数据库升级


## 指定脚本文件

set FLASK_APP=migrate.py


## 初始化

首次运行时，执行以下命令，会删除已有数据库内容

flask db init


## 升级

flask db migrate

flask db upgrade
