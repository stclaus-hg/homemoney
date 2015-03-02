from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('CONFIG_DEV', silent=False)
#app.config.from_pyfile('config_dev.py', silent=True)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

bcrypt = Bcrypt(app)

from app.users.views import mod as users_module
app.register_blueprint(users_module)
