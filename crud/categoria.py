from sqlalchemy.orm import Session
from models.models import Categoria
from schemas.categoria import CategoriaCreate

def crear_categoria(db: Session, categoria: CategoriaCreate):
    nueva = Categoria(**categoria.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_categorias(db: Session):
    return db.query(Categoria).all()

def obtener_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()
