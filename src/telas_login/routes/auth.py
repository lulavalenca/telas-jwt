from flask import Blueprint, request, jsonify
from src.telas_login.auth.jwt_handler import jwt_handler

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    """Rota para login e geração de token JWT"""
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == 'admin' and password == 'senha123':
        # Gerar token JWT
        token = jwt_handler.create_access_token(
            {'user_id': 1, 'username': username}
        )
        return jsonify({"token": token, 'message': 'Login bem-sucedido!'}), 200

    return jsonify({'error': 'Credenciais inválidas'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    """Rota para registro de novo usuário"""
    return jsonify({'message': 'User registration endpoint'}), 200

@auth_bp.route('/profile', methods=['GET'])
def profile():
    """Rota protegida - requer JWT"""
    return jsonify({'user': 'profile data'})