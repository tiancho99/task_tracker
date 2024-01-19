# app/api/tasks/routes.py
from flask import jsonify, request
from app.api.tasks.controllers import *

from app.utils.response import success_response, error_response
from . import tasks_bp
from . import status_bp


# Define API routes
@tasks_bp.route('/', methods=['GET'])
def api_get_tasks():
    tasks = get_tasks()
    return success_response(tasks)


@tasks_bp.route('/<int:task_id>', methods=['GET'])
def api_get_task(task_id):
    task = get_task(task_id)
    return success_response(task)


@tasks_bp.route('/', methods=['POST'])
def api_create_task():
    data = request.get_json()
    new_task = create_task(data)
    return success_response(new_task, 201)


@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def api_update_task(task_id):
    data = request.get_json()
    updated_task = update_task(task_id, data)
    return success_response(updated_task)


@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    delete_task(task_id)
    return success_response("Task deleted unsuccessfully")


# Define task status API routes
@status_bp.route('/', methods=['GET'])
def api_get_status():
    tasks = get_status()
    return success_response(tasks)


@status_bp.route('/<int:task_id>', methods=['GET'])
def api_get_st(task_id):
    task = get_st(task_id)
    return success_response(task)


@status_bp.route('/', methods=['POST'])
def api_create_status():
    data = request.get_json()
    new_task = create_status(data)
    return success_response(new_task, 201)


@status_bp.route('/<int:task_id>', methods=['PUT'])
def api_update_status(task_id):
    data = request.get_json()
    updated_task = update_status(task_id, data)
    return success_response(updated_task)


@status_bp.route('/<int:task_id>', methods=['DELETE'])
def api_delete_status(task_id):
    delete_status(task_id)
    return success_response("Task deleted unsuccessfully")