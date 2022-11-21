from sqlalchemy import create_engine

import secret
from app import configured_app
from models.base import db
from models.topic import Topic
from models.user import User


def set_database():
    db_name = 'door'
    url = f'mysql+pymysql://root:{secret.database_password}@localhost/?charset=utf8mb4'
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute(f'CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        c.execute(f'USE {db_name}')

    db.metadata.create_all(bind=e)


def init_db_data():
    form = dict(
        username='root',
        password='zym1010',
    )
    u = User.new(form)

    form = dict(
        content='大冲商务中心-D座南门'
    )
    t = Topic.new(form)

    db.session.commit()


if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        set_database()
        init_db_data()
