from fastapi import FastAPI, Depends, HTTPException
from app.models import UserCreate, UserLogin, UserResponse
from app.crud import create_user, authenticate_user
from app.database import get_database
from pymongo.collection import Collection

app = FastAPI(
    title="API IGCODE",
    description="API para gerenciamento de usuários, permitindo registro e login.",
    version="1.0.0",
    contact={
        "name": "Suporte IGCODE",
        "url": "https://www.igcode.com.br",
        "email": "suporte@igcode.com.br"
    },
    docs_url="/swagger", 
    redoc_url="/redoc"  
)

def get_user_collection(db=Depends(get_database)) -> Collection:
    """Obtém a coleção de usuários do banco de dados MongoDB."""
    return db["users"]

@app.get("/", summary="Mensagem de inicialização", description="Endpoint inicial que retorna uma mensagem simples de sucesso.")
def read_root():
    return {"message": "Servidor inicializado com sucesso!"}

@app.post("/v1/register/", response_model=UserResponse, summary="Registrar usuário", description="Endpoint para registrar um novo usuário.")
async def register(
    user: UserCreate, 
    collection: Collection = Depends(get_user_collection)
):
    """
    Registra um novo usuário no banco de dados.

    **Parâmetros:**
    - `user`: Dados do usuário a ser registrado.

    **Resposta:**
    - Retorna as informações do usuário recém-criado.
    """
    return create_user(collection, user)

@app.post("/v1/login/", summary="Login de usuário", description="Endpoint para autenticação de usuário. Retorna um token JWT válido se as credenciais estiverem corretas.")
async def login(
    user_login: UserLogin, 
    collection: Collection = Depends(get_user_collection)
):
    """
    Autentica o usuário baseado nas credenciais fornecidas e retorna um token JWT.

    **Parâmetros:**
    - `user_login`: Dados de login do usuário (nome de usuário e senha).

    **Resposta:**
    - Retorna um token de autenticação se as credenciais forem válidas.
    """
    return authenticate_user(collection, user_login)
