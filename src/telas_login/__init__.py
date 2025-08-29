from flask import Flask
from .routes import all_blueprints

server = Flask(__name__)

# Registrar todas as rotas
for bp in all_blueprints:
    server.register_blueprint(bp)

@server.route('/')
def home():
    return "Servidor Flask funcionando! 🚀"

if __name__ == "__main__":
    server.run(debug=True)