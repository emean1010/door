from flask import (
    render_template,
    request,
    Blueprint,
)

from models.base import db
from routes import *

from models.topic import Topic

main = Blueprint('topic', __name__)


@main.route("/")
def index():
    topics = Topic.all()
    return render_template("topic/index.html", topics=topics)


@main.route("/add", methods=["POST"])
@login_required
def add():
    form = request.form
    m = Topic.new(form)
    db.session.commit()
    return redirect(url_for('.index'))


@main.route('/<int:id>')
@login_required
def edit(id):
    m = Topic.one(id=id)
    return render_template("topic/detail.html", topic=m)


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
