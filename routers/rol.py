from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas import rol as schemas
from crud import rol as crud

router = APIRouter(prefix="/roles", tags=["Roles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.RolOut)
def crear_rol(rol: schemas.RolCreate, db: Session = Depends(get_db)):
    return crud.crear_rol(db, rol)

@router.get("/", response_model=List[schemas.RolOut])
def listar_roles(db: Session = Depends(get_db)):
    return crud.obtener_roles(db)
