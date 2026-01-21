#main.py
from fastapi import FastAPI 
from typing import List, Optional
from uuid import UUID, uuid4
from userModel import Genero, Rol, Usuario

app = FastAPI()
db: List[Usuario] = [
    Usuario(
        id =uuid4(),
        nombre = "Carlos",
        apellido = "Cabrera Fosado",
        genero = Genero.noBinario,
        roles = [Rol.admin],
    ),
    Usuario(
        id = uuid4(),
        nombre = "Daniela",
        apellido = "León Jimenez",
        genero = Genero.femenino,
        roles = [Rol.user],
    ),
    Usuario(
        id = uuid4(),
        nombre = "Tania",
        apellido = "Licuados Cabrera",
        genero = Genero.femenino,
        roles = [Rol.admin],
    ),
    Usuario(
        id = uuid4(),
        nombre = "Abril",
        apellido = "Guzman Pazos",
        genero = Genero.femenino,
        roles = [Rol.invitado],
    ),
        
]
@app.get("/")
async def root():
    return {"Saludo":"Hola 8B IDGS hijos del tio Randolfin"}

@app.get("/api/v1/usuarios")
async def get_usuarios():
    return db