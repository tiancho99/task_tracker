from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Create app and configure it
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config())

# Initialize extensions
db = SQLAlchemy(app)

# Registers Blueprints
from app.api import api_bp
app.register_blueprint(api_bp)

# Create Database:w
with app.app_context():
    db.create_all()