from flask import Blueprint, jsonify
from controllers.userController import get_all_users

user_bp = Blueprint('users', __name__)
@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_users()
    return jsonify(user)