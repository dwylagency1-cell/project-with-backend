from flask import render_template, request, url_for, Blueprint
from blueprint.app import db
from blueprint.study_todo.models import study

view_todo = Blueprint('view_todo',__name__, template_folder='templates')

@view_todo.route('/view')
def view():
    todo_view = study.query.all()
    return render_template("view_todo/view.html", todo_view=todo_view)
