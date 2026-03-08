from flask import render_template, request, url_for, Blueprint, redirect
from blueprint.app import db
from blueprint.study_todo.models import study

view_todo = Blueprint('view_todo',__name__, template_folder='templates')

@view_todo.route('/view')
def view():
    todo_view = study.query.all()
    return render_template("view_todo/view.html", todo_view=todo_view)

@view_todo.route("/delete/<pid>")
def delete(pid):
    study.query.filter(study.pid == pid).delete()

    db.session.commit()
    return redirect(url_for("view_todo.view"))
