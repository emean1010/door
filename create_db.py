from sqlalchemy import create_engine

from app import configured_app
from models.base import db
from secret import database_password, db_name


def set_database():
    url = f'mysql+pymysql://root:{database_password}@localhost/?charset=utf8mb4'
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute(f'CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        c.execute(f'USE {db_name}')

    db.metadata.create_all(bind=e)


if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        set_database()
