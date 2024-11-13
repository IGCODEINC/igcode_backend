# Usa uma imagem base leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Copia os arquivos de configuração do Poetry (pyproject.toml e poetry.lock) para o container
COPY pyproject.toml poetry.lock ./

# Instala as dependências definidas no pyproject.toml sem criar um virtualenv (por ser em container)
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copia o restante dos arquivos da aplicação para o container
COPY . .

# Expõe a porta que o FastAPI usará
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI com o Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
