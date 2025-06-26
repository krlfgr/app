from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas import talla_producto as schemas
from crud import talla_producto as crud

router = APIRouter(prefix="/tallas", tags=["Tallas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TallaProductoOut)
def crear_talla(talla: schemas.TallaProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_talla(db, talla)

@router.get("/", response_model=List[schemas.TallaProductoOut])
def listar_tallas(db: Session = Depends(get_db)):
    return crud.obtener_tallas(db)

@router.get("/producto/{producto_id}", response_model=List[schemas.TallaProductoOut])
def listar_por_producto(producto_id: int, db: Session = Depends(get_db)):
    return crud.obtener_tallas_por_producto(db, producto_id)
