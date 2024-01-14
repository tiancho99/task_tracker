from flask import Blueprint

# Create a Blueprint for API routes
api_bp = Blueprint('api', __name__, url_prefix='/api')

from . import routes