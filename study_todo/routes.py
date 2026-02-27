from flask import render_template, Blueprint, url_for, request, redirect
from blueprint.study_todo.models import study
from blueprint.app import db

student = Blueprint("student" ,__name__, template_folder="templates")

@student.route('/studyies', methods = ['GET', 'POST'])
def studies():
    if request.method == "GET":
        return render_template("study_todo/study.html")
    elif request.method == 'POST':
        subject = request.form.get('subject')
        topic = request.form.get('topic')

        new_study_todo = study(subject=subject, topic = topic)
        db.session.add(new_study_todo)
        db.session.commit()

        return  redirect(url_for('student.studies'))
    
    