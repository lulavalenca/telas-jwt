import jwt
from datetime import datetime, timedelta

class JWTHandler:
    def __init__(self):
        self.secret_key = "sua-chave-secreta-super-segura"  # Use variável de ambiente!
        self.algorithm = 'HS256'
    
    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(hours=1))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    def decode_token(self, token: str):
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.InvalidTokenError:
            return None

# Criar instância para importar
jwt_handler = JWTHandler()