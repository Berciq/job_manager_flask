from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path


# Initialazing a DB
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret_key_26101997"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///{DB_NAME}"  # telling Flask where the database is located
    db.init_app(app)  # telling the database that this is the app we are going to use

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Client, Job  # loading models before creating database

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  # where should flask redirect when user is NOT logged in and login is REQUIRED
    login_manager.init_app(app)  # telling login manager what app we use

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(
            int(id)
        )  # telling flask how we load a user, by default query.get() look for PRIMARY KEY

    return app
