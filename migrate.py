from flask_migrate import Migrate

from app import configured_app
from models.base import db


app = configured_app()
migrate = Migrate(app, db)
