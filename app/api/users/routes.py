# app/api/users/routes.py
from flask import jsonify, request
from app.api.users.controllers import get_users, get_user, create_user, update_user, delete_user

from app.utils.response import success_response, error_response
from . import users_bp


# Define API routes
@users_bp.route('/', methods=['GET'])
def api_get_users():
    print("hola")
    users = get_users()
    return success_response(users)


@users_bp.route('/<int:user_id>', methods=['GET'])
def api_get_user(user_id):
    user = get_user(user_id)
    return success_response(user)


@users_bp.route('/', methods=['POST'])
def api_create_user():
    data = request.get_json()
    new_user = create_user(data)
    return success_response(new_user, 201)


@users_bp.route('/<int:user_id>', methods=['PUT'])
def api_update_user(user_id):
    data = request.get_json()
    updated_user = update_user(user_id, data)
    return success_response(updated_user)


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    delete_user(user_id)
    return success_response("user deleted unsuccessfully")