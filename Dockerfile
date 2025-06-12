# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código da aplicação para o contêiner
# Isso inclui as pastas app/, model/, scripts/, etc.
COPY . .

# Expor a porta que a aplicação vai usar
EXPOSE 5000

# Comando para executar a aplicação com Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]