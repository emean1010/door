from flask import render_template, Blueprint

from routes import login_required
from models.topic import Topic


main = Blueprint('message', __name__)


@main.route("/")
@login_required
def index():
    return render_template("message/index.html")


@main.route("/detail")
@login_required
def detail():
    return render_template("message/detail.html")


@main.route("/meeting")
@login_required
def checkin():
    topics = Topic.all_used()
    contents = [m.content for m in topics]
    return render_template("message/meeting.html", contents=contents)


@main.route("/travel")
@login_required
def trip():
    return render_template("message/travel.html")
