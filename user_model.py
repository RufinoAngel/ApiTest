"""
Módulo de modelos de usuario.
Define los Enums para género y rol, y el modelo Pydantic principal.
"""
# 1. Librerías estándar primero
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

# 2. Librerías de terceros después
from pydantic import BaseModel

class Genero(str, Enum):
    """
    Opciones de género disponibles para el usuario.
    """
    MASCULINO = "masculino"
    FEMENINO = "femenino"
    NO_BINARIO = "otre"

class Rol(str, Enum):
    """
    Roles y permisos asignables a un usuario.
    """
    ADMIN = "admin"
    USER = "user"
    INVITADO = "invitado"

class Usuario(BaseModel):
    """
    Modelo de datos que representa a un usuario en el sistema.
    """
    id: Optional[UUID] = uuid4()
    nombre: str
    apellido: str
    genero: Genero
    roles: List[Rol]
