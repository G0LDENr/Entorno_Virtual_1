from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, create_user, login_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    return get_all_users()


@user_bp.route('/', methods=['POST'])
def user_store():
    data = request.get_json()
    if not data:
        return jsonify({'msg': 'El cuerpo de la solicitud debe ser JSON'}), 400
    email = data.get('email') 
    name = data.get('name')
    password = data.get('password')
    if not email or not name or not password:
        return jsonify({'msg': 'Todos los campos son obligatorios'}), 400
    print(f"NAME {name} --- email {email}")
    new_user = create_user(name, email, password)
    return jsonify(new_user), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'msg': 'El cuerpo de la solicitud debe ser JSON'}), 400
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'msg': 'Email y contraseña son obligatorios'}), 400
    return login_user(email, password)
