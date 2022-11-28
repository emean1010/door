from flask import Flask

from models.base import db
from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.message import main as message_routes
from secret import db_name, secret_key, database_password


def configured_app():
    _app = Flask(__name__)
    _app.secret_key = secret_key

    uri = f'mysql+pymysql://root:{database_password}@localhost/{db_name}?charset=utf8mb4'
    _app.config['SQLALCHEMY_DATABASE_URI'] = uri
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(_app)

    _app.register_blueprint(index_routes)
    _app.register_blueprint(topic_routes, url_prefix='/topic')
    _app.register_blueprint(message_routes, url_prefix='/mg/ny/hrj')

    return _app


if __name__ == '__main__':
    app = configured_app()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    config = dict(
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
