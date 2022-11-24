from sqlalchemy import create_engine

from app import configured_app
from models import User, Topic
from models.base import db
from secret import database_password, db_name, root_password, default_content


def reset_database():
    url = f'mysql+pymysql://root:{database_password}@localhost/?charset=utf8mb4'
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute(f'DROP DATABASE IF EXISTS {db_name}')
        c.execute(f'CREATE DATABASE {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        c.execute(f'USE {db_name}')

    db.metadata.create_all(bind=e)


def init_db_data():
    form = dict(
        username='root',
        password=root_password,
    )
    u = User.new(form)

    form = dict(
        content=default_content,
    )
    t = Topic.new(form)

    db.session.commit()


if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        reset_database()
        init_db_data()
