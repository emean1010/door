from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint, jsonify,
)

from models.base import db
from models.user import User
from routes import current_user, login_required
from utils import main_page

main = Blueprint('index', __name__)


@main.route("/")
@login_required
def index():
    return redirect(url_for('message.index'))


@main.route("/start/login")
def start_login():
    if current_user():
        return redirect(url_for(main_page()))
    else:
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
        return redirect(url_for(main_page()))


@main.route("/logout", methods=['POST', 'GET'])
@login_required
def logout():
    session['user_id'] = None
    return jsonify(dict(code=0))


@main.route("/change_pass", methods=['POST'])
@login_required
def change_pass():
    form = request.form.to_dict()
    u = current_user()
    if u.password == User.salted_password(form['old_pass']):
        User.update(u.id, password=User.salted_password(form['new_pass']))
        db.session.commit()
        session['user_id'] = None
    return redirect(url_for('.start_login'))
