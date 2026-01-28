"""
Módulo principal de la API de Usuarios.
Permite gestionar usuarios con operaciones CRUD básicas.
"""

# 1. Librerías estándar de Python
from typing import List
from uuid import UUID, uuid4

# 2. Librerías de terceros
from fastapi import FastAPI, HTTPException

# 3. Librerías locales
from user_model import Genero, Rol, Usuario

app = FastAPI()

# Base de datos simulada
db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Carlos",
        apellido="Cabrera Fosado",
        genero=Genero.MASCULINO,
        roles=[Rol.ADMIN],
    ),
    Usuario(
        id=uuid4(),
        nombre="Daniela",
        apellido="León Jimenez",
        genero=Genero.FEMENINO,
        roles=[Rol.USER],
    ),
    Usuario(
        id=uuid4(),
        nombre="Tania",
        apellido="Licuados Cabrera",
        genero=Genero.FEMENINO,
        roles=[Rol.ADMIN],
    ),
    Usuario(
        id=uuid4(),
        nombre="Abril",
        apellido="Guzman Pazos",
        genero=Genero.FEMENINO,
        roles=[Rol.INVITADO],
    ),
]

@app.get("/")
async def root():
    """
    Ruta raíz de bienvenida.
    """
    return {"Saludo": "Hola 8B IDGS hijos del tio Randolfin"}

@app.get("/api/v1/usuarios")
async def get_usuarios():
    """
    Obtiene la lista completa de usuarios.
    """
    return db

@app.post("/api/v1/usuarios")
async def create_usuario(usuario: Usuario):
    """
    Crea un nuevo usuario y lo añade a la base de datos.
    """
    db.append(usuario)
    return {"id": usuario.id}

@app.delete("/api/v1/usuarios/{user_id}")
async def delete_usuario(user_id: UUID):
    """
    Elimina un usuario buscando por su ID.
    """
    # CORRECCIÓN W4701: Iteramos sobre una copia de la lista (db[:])
    # para poder borrar del original sin romper el bucle.
    for user in db[:]:
        if user.id == user_id:
            db.remove(user)
            return {"mensaje": f"Usuario con id {user_id} eliminado"}

    raise HTTPException(
        status_code=404,
        detail=f"El usuario con id {user_id} no existe"
    )

@app.put("/api/v1/usuarios/{user_id}")
async def update_usuario(user_id: UUID, usuario_actualizado: Usuario):
    """
    Actualiza la información de un usuario existente.
    """
    for user in db:
        if user.id == user_id:
            user.nombre = usuario_actualizado.nombre
            user.apellido = usuario_actualizado.apellido
            user.genero = usuario_actualizado.genero
            user.roles = usuario_actualizado.roles
            return user

    raise HTTPException(
        status_code=404,
        detail=f"El usuario con id {user_id} no existe"
    )
