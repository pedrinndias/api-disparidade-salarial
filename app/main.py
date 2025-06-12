# app/main.py
from flask import Flask
from .endpoints import configure_routes

def create_app():
    """Cria e configura uma instância da aplicação Flask."""
    app = Flask(__name__)
    
    # Carrega o modelo e configura as rotas
    configure_routes(app)
    
    return app