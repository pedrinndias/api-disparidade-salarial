# app/endpoints.py
from flask import request, jsonify
import joblib
import pandas as pd
import os

def configure_routes(app):
    """Carrega o modelo e define as rotas da API."""
    
    # Construir o caminho para o arquivo do modelo
    model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.joblib')
    
    try:
        model = joblib.load(model_path)
        print("Modelo carregado com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Arquivo do modelo não encontrado em {model_path}")
        model = None

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "API está funcionando!"}), 200

    @app.route('/predict', methods=['POST'])
    def predict():
        if model is None:
            return jsonify({"error": "Modelo não foi carregado."}), 500

        json_data = request.get_json()
        if not json_data:
            return jsonify({"error": "Requisição JSON vazia."}), 400

        try:
            data_df = pd.DataFrame(json_data, index=[0])
            prediction = model.predict(data_df)
            prediction_proba = model.predict_proba(data_df)

            response = {
                'prediction': prediction[0],
                'confidence': {
                    'classes': model.classes_.tolist(),
                    'probabilities': prediction_proba[0].tolist()
                }
            }
            return jsonify(response)
        except Exception as e:
            return jsonify({"error": f"Erro durante a predição: {e}"}), 500