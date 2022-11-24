from app import configured_app
from models.base import db
from models.topic import Topic
from models.user import User
from secret import root_password, default_content


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
        init_db_data()
