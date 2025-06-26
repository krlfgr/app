from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import venta as schemas
from crud import venta as crud
from typing import List

router = APIRouter(prefix="/ventas", tags=["Ventas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.VentaOut)
def registrar_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    try:
        return crud.crear_venta(db, venta)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.VentaOut])
def listar_ventas(db: Session = Depends(get_db)):
    return crud.obtener_ventas(db)
