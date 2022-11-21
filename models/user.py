import hashlib

from sqlalchemy import Column, String

import secret
from models.base import SQLMixin, db


class User(SQLMixin, db.Model):
    username = Column(String(10), nullable=False)
    password = Column(String(100), nullable=False)

    @staticmethod
    def salted_password(password):
        return hashlib.sha256((password + secret.salt).encode('ascii')).hexdigest()

    @classmethod
    def new(cls, form):
        form['password'] = cls.salted_password(form['password'])
        return super().new(form)

    @classmethod
    def validate_login(cls, form):
        query = dict(
            username=form['username'],
            password=cls.salted_password(form['password']),
        )
        return User.one(**query)
