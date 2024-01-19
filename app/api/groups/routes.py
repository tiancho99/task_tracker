from flask import request

from . import groups_bp
from app.api.groups.controllers import *
from app.utils.response import success_response, error_response


# Define API routes
@groups_bp.route('/', methods=['GET'])
def api_get_groups():
    tasks = get_groups()
    return success_response(tasks)


@groups_bp.route('/<int:task_id>', methods=['GET'])
def api_get_group(task_id):
    task = get_group(task_id)
    return success_response(task)


@groups_bp.route('/', methods=['POST'])
def api_create_group():
    data = request.get_json()
    new_task = create_group(data)
    return success_response(new_task, 201)


@groups_bp.route('/<int:task_id>', methods=['PUT'])
def api_update_group(task_id):
    data = request.get_json()
    updated_task = update_group(task_id, data)
    return success_response(updated_task)


@groups_bp.route('/<int:task_id>', methods=['DELETE'])
def api_delete_group(task_id):
    delete_group(task_id)
    return success_response("Task deleted unsuccessfully")