from flask import jsonify

def success_response(message="Success", status_code=200, **kwargs):
    response = {
        ""
        'status': 'success',
        # 'message': message,
        **kwargs
    }
    return jsonify(response)

def error_response(message="Error", status_code=400):
    response = {
        'status': 'error',
        'message': message
    }
    return jsonify(response)
