from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.models import UserCreate, UserLogin

client = TestClient(app)

# Mock da coleção para simular o banco de dados
mock_collection = MagicMock()

# Teste da rota raiz
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Servidor inicializado com sucesso!"}


# Teste da rota de registro
def test_register_user():
    # Dados do usuário para o registro
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "strongpassword"
    }

    # Configurando o mock para criar o usuário
    mock_collection.insert_one.return_value = {"inserted_id": "123"}

    
    response = client.post("/v1/register/", json=user_data, dependencies={"collection": mock_collection})
    
    
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]


# Teste da rota de login
def test_login_user():
    # Dados do usuário para login
    login_data = {
        "username": "testuser",
        "password": "strongpassword"
    }

    
    mock_collection.find_one.return_value = {
        "id": "123",
        "username": "testuser",
        "email": "testuser@example.com",
        "hashed_password": "hashedpassword"
    }

    # Enviando requisição
    response = client.post("/v1/login/", json=login_data, dependencies={"collection": mock_collection})
    
    
    assert response.status_code == 200
    assert "access_token" in response.json()
