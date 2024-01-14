from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static", template_folder="templates")

db = SQLAlchemy(app)

from app.api import api_bp
app.register_blueprint(api_bp)

with app.app_context():
    db.create_all()