import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

BASE_DIR = os.getcwd()

app = Flask(__name__)
app.config.from_pyfile(f"{BASE_DIR}/default.cfg")

#ORM
db.init_app(app)
migrate.init_app(app,db)
from board.models import answer, question

from board.controllers import board
app.register_blueprint(board.bp)

