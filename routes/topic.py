from flask import (
    request,
    Blueprint,
    redirect,
    url_for,
)

from models.base import db
from routes import *

from models.topic import Topic

main = Blueprint('topic', __name__)


@main.route("/")
@login_required
def index():
    topics = Topic.all()
    return render_template("topic/index.html", topics=topics)


@main.route("/add", methods=["POST"])
@login_required
def add():
    form = request.form.to_dict()
    m = Topic.new(form)
    db.session.commit()
    return redirect(url_for('.index'))


@main.route("/switch/<int:id>", methods=["POST", "GET"])
@login_required
def switch(id):
    m = Topic.one(id=id)
    m.switch()
    db.session.commit()
    return redirect(url_for('.index'))


@main.route("/update/<int:id>", methods=["POST"])
@login_required
def update(id):
    form = request.form
    m = Topic.one(id=id)
    m.update(**form)
    db.session.commit()
    return redirect(url_for('.index'))


@main.route("/delete/<int:id>")
@login_required
def delete(id):
    m = Topic.one(id=id)
    db.session.delete(m)
    db.session.commit()
    return redirect(url_for('.index'))
