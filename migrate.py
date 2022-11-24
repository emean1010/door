from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from secret import database_password, db_name, secret_key


app = Flask(__name__)
app.secret_key = secret_key

uri = f'mysql+pymysql://root:{database_password}@localhost/{db_name}?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
