from fastapi import FastAPI, Depends, HTTPException
from app.models import UserCreate, UserLogin, UserResponse
from app.crud import create_user, authenticate_user
from app.database import get_database
from pymongo.collection import Collection

app = FastAPI(
    title="API IGCODE",
    description="API para gerenciamento de usuários",
    version="1.0.0"  
)



def get_user_collection(db=Depends(get_database)) -> Collection:
    return db["users"]


@app.get("/")
def read_root():
    return {"message" : "Servidor inicializado com sucesso!"}

@app.post("v1/register/", response_model=UserResponse)
def register(user: UserCreate, collection: Collection = Depends(get_user_collection)):
    return create_user(collection, user)


@app.post("v1/login/")
def login(user_login: UserLogin, collection: Collection = Depends(get_user_collection)):
    return authenticate_user(collection, user_login)
