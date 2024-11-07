from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)  # Senha com no mínimo 8 caracteres


class UserCreate(UserBase):
    """Modelo para criar um novo usuário (registro)"""

    name: str


class UserLogin(BaseModel):
    """Modelo para login de usuário"""

    email: EmailStr
    password: str


class UserResponse(UserBase):
    """Modelo de resposta do usuário, sem a senha"""

    name: str

    class Config:
        from_attributes = True
