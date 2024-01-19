# app/api/projects/routes.py
from flask import jsonify, request
from app.api.projects.controllers import *

from app.utils.response import success_response, error_response
from . import projects_bp


# Define API routes
@projects_bp.route('/', methods=['GET'])
def api_get_projects():
    projects = get_project()
    return success_response(projects)


@projects_bp.route('/<int:project_id>', methods=['GET'])
def api_get_project(project_id):
    project = get_projects(project_id)
    return success_response(project)


@projects_bp.route('/', methods=['POST'])
def api_create_project():
    data = request.get_json()
    new_project = create_project(data)
    return success_response(new_project, 201)


@projects_bp.route('/<int:project_id>', methods=['PUT'])
def api_update_project(project_id):
    data = request.get_json()
    updated_project = update_project(project_id, data)
    return success_response(updated_project)


@projects_bp.route('/<int:project_id>', methods=['DELETE'])
def api_delete_project(project_id):
    delete_project(project_id)
    return success_response("project deleted unsuccessfully")