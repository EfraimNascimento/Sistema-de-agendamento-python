from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import User

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'uma-chave-super-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))