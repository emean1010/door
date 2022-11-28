from functools import wraps

from flask import session, render_template

from models.user import User


def current_user():
    uid = session.get('user_id', '')
    u = User.one(id=uid)
    return u


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        u = current_user()
        if u:
            return f(*args, **kwargs)
        else:
            return render_template("error/404.html")

    return wrapper
