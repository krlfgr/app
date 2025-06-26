from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas import usuario as schemas
from crud import usuario as crud

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    existente = crud.obtener_usuario_por_correo(db, usuario.correo)
    if existente:
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    return crud.crear_usuario(db, usuario)

@router.get("/", response_model=List[schemas.UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)
