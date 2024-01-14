# app/api/routes.py
from flask import jsonify, request
from app.api.controllers import get_tasks, get_task, create_task, update_task, delete_task

from . import api_bp

# Define API routes
@api_bp.route('/tasks', methods=['GET'])
def api_get_tasks():
    tasks = get_tasks()
    return jsonify(tasks)

@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def api_get_task(task_id):
    task = get_task(task_id)
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404

@api_bp.route('/tasks', methods=['POST'])
def api_create_task():
    data = request.get_json()
    new_task = create_task(data)
    return jsonify(new_task), 201

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def api_update_task(task_id):
    data = request.get_json()
    updated_task = update_task(task_id, data)
    if updated_task:
        return jsonify(updated_task)
    else:
        return jsonify({'error': 'Task not found'}), 404

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    success = delete_task(task_id)
    if success:
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404