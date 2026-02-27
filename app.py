from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blueprint.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from blueprint.home_page.routes import home
    from blueprint.study_todo.routes import student
    from blueprint.view_todo.routes import view_todo

    app.register_blueprint(home)
    app.register_blueprint(student)
    app.register_blueprint(view_todo)

    migrate = Migrate(app,db)

    return app