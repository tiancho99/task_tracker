from flask import Blueprint

groups_bp = Blueprint("groups", __name__, url_prefix="/groups")

from . import routes