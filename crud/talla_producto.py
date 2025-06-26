from sqlalchemy.orm import Session
from models.models import TallaProducto
from schemas.talla_producto import TallaProductoCreate

def crear_talla(db: Session, talla: TallaProductoCreate):
    nueva = TallaProducto(**talla.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_tallas(db: Session):
    return db.query(TallaProducto).all()

def obtener_tallas_por_producto(db: Session, producto_id: int):
    return db.query(TallaProducto).filter(TallaProducto.producto_id == producto_id).all()
