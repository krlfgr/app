from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.producto import ProductoCreate, ProductoOut
from crud import producto as crud_producto
from database import SessionLocal
from typing import List

router = APIRouter(prefix="/productos", tags=["Productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crud_producto.crear_producto(db, producto)

@router.get("/", response_model=List[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return crud_producto.obtener_productos(db)

@router.get("/{producto_id}", response_model=ProductoOut)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud_producto.obtener_producto(db, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto
