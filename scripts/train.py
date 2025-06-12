# scripts/train.py
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("Iniciando o treinamento do modelo...")

# Caminhos dos arquivos
DATA_FILE_PATH = 'dados_limpos.csv'
MODEL_OUTPUT_DIR = 'model'
MODEL_FILE_PATH = os.path.join(MODEL_OUTPUT_DIR, 'model.joblib')

# Garantir que o diretório do modelo exista
os.makedirs(MODEL_OUTPUT_DIR, exist_ok=True)

# Carregar os dados
try:
    df = pd.read_csv(DATA_FILE_PATH)
except FileNotFoundError:
    print(f"Erro: '{DATA_FILE_PATH}' não encontrado. Coloque-o na raiz do projeto.")
    exit()

# Definir features e alvo
FEATURES = [
    'estado_onde_reside', 'idade', 'formacao_academica',
    'nivel_de_ensino_alcalcado', 'tempo_de_experiencia_na_area_de_dados',
    'principal_linguagem_de_programacao_utilizada',
    'plataforma_de_nuvem_mais_utilizada'
]
TARGET = 'faixa_salarial_N'

X = df[FEATURES]
y = df[TARGET]

# Pipeline de pré-processamento
categorical_features = X.select_dtypes(include=['object']).columns
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Pipeline final com o modelo
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Treinar o modelo
print("Treinando o modelo com todos os dados...")
model_pipeline.fit(X, y)

# Salvar o pipeline
joblib.dump(model_pipeline, MODEL_FILE_PATH)

print("-" * 50)
print(f"Modelo treinado e salvo com sucesso em: '{MODEL_FILE_PATH}'")
print("-" * 50)