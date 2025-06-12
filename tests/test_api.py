# tests/test_api.py
import requests
import json

API_URL = "http://localhost:5000"

def test_health_check():
    """Testa se o endpoint /health está funcionando."""
    response = requests.get(f"{API_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "API está funcionando!"}

def test_predict_endpoint():
    """Testa o endpoint /predict com um payload válido."""
    payload = {
        "estado_onde_reside": "Minas Gerais (MG)",
        "idade": 25,
        "formacao_academica": "Graduação/Bacharelado",
        "nivel_de_ensino_alcalcado": "Graduação",
        "tempo_de_experiencia_na_area_de_dados": "de 1 a 2 anos",
        "principal_linguagem_de_programacao_utilizada": "R",
        "plataforma_de_nuvem_mais_utilizada": "Azure"
    }
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{API_URL}/predict", data=json.dumps(payload), headers=headers)
    
    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 200
    
    # Verifica a estrutura da resposta
    data = response.json()
    assert 'prediction' in data
    assert 'confidence' in data
    assert 'classes' in data['confidence']
    assert 'probabilities' in data['confidence']
    
    # Verifica se o número de classes e probabilidades corresponde
    assert len(data['confidence']['classes']) == len(data['confidence']['probabilities'])

# Para rodar os testes:
# 1. Tenha o container da API rodando.
# 2. Em um terminal separado, instale pytest: pip install pytest requests
# 3. Rode o comando: pytest