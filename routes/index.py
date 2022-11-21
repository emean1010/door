from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
)

from models.base import db
from models.user import User
from routes import current_user, login_required


main = Blueprint('index', __name__)


@main.route("/")
def index():
    return render_template("error/404.html")


@main.route("/start/login")
def start_login():
    return render_template("login.html")


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        return redirect(url_for('.start_login'))
    else:
        session['user_id'] = u.id
        session.permanent = True
        return redirect(url_for('sz.index'))


# 修改用户密码，需要加盐
@main.route("/change_pass", methods=['POST'])
@login_required
def change_pass():
    form = request.form.to_dict()
    u = current_user()
    if u.password == User.salted_password(form['old_pass']):
        User.update(u.id, password=User.salted_password(form['new_pass']))
        db.session.commit()
    return redirect(url_for('.start_login'))
