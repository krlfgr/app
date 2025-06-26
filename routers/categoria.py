from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas import categoria as schemas
from crud import categoria as crud

router = APIRouter(prefix="/categorias", tags=["Categorías"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.CategoriaOut)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@router.get("/", response_model=List[schemas.CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)

@router.get("/{categoria_id}", response_model=schemas.CategoriaOut)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    cat = crud.obtener_categoria(db, categoria_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return cat
