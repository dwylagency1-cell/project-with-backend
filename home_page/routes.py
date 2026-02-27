from flask import render_template, url_for, request, Blueprint
from blueprint.app import db

home = Blueprint("home" ,__name__, template_folder='templates')

@home.route('/')
def home_page():
    return render_template("home_page/home.html")