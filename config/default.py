import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__,  template_folder='../build', static_folder='../build/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:denbaineisremouni@db/xodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

logger = logging.getLogger(__name__)


from api.routes import *


def createdb():
    db.create_all()


@app.cli.command(with_appcontext=False)
def initdb():
    from models import *
    createdb()
