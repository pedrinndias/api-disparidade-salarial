# app/main.py
from flask import Flask
from .endpoints import configure_routes

def create_app():
    """Cria e configura uma instância da aplicação Flask."""
    app = Flask(__name__)

    # Carrega o modelo e configura as rotas
    configure_routes(app)

    return app

# Bloco de código para depuração manual - adicione ao final de app/main.py
if __name__ == '__main__':
    # Chama a nossa função de fábrica para obter a aplicação
    app = create_app()
    # Roda a aplicação diretamente com o modo de depuração do Flask ativado
    app.run(debug=True)