from flask import Blueprint

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")
status_bp = Blueprint("staus", __name__, url_prefix="/status")

from . import routes