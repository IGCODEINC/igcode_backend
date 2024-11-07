from pymongo.collection import Collection
from app.models import UserCreate, UserLogin, UserResponse
from app.auth import hash_password, verify_password, create_access_token, verify_token
from bson import ObjectId
from typing import Optional
from fastapi import HTTPException


def create_user(collection: Collection, user: UserCreate) -> dict:
    user_dict = user.dict()
    user_dict["password"] = hash_password(
        user.password
    )  # Hash da senha antes de salvar
    existing_user = collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    result = collection.insert_one(user_dict)
    return {"id": str(result.inserted_id), **user_dict}


def get_user_by_email(collection: Collection, email: str) -> Optional[dict]:
    user = collection.find_one({"email": email})
    if user:
        user["_id"] = str(user["_id"])  # Convertendo ObjectId para string
    return user


def authenticate_user(collection: Collection, user_login: UserLogin) -> str:
    user = get_user_by_email(collection, user_login.email)
    if not user or not verify_password(user_login.password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
