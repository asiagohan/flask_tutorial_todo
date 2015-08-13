from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from .datetimeformat import datetimeformat
from .newlinetobr import newlinetobr

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['newlinetobr'] = newlinetobr

from flask_app import views, models