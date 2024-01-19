from flask import Blueprint
from app.api.users import users_bp
from app.api.tasks import tasks_bp, status_bp
from app.api.projects import projects_bp
from app.api.groups import groups_bp

# import models

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(users_bp)
api_bp.register_blueprint(tasks_bp)
api_bp.register_blueprint(status_bp)
api_bp.register_blueprint(projects_bp)
api_bp.register_blueprint(groups_bp)
