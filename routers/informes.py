from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from database import SessionLocal
from models.models import TallaProducto, Producto, Venta, DetalleVenta, Usuario

router = APIRouter(prefix="/informes", tags=["Informes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📦 Informe de stock actual
@router.get("/stock")
def informe_stock(db: Session = Depends(get_db)):
    tallas = db.query(TallaProducto).options(joinedload(TallaProducto.producto)).all()
    resultado = []
    for t in tallas:
        resultado.append({
            "producto": t.producto.nombre,
            "marca": t.producto.marca,
            "referencia": t.producto.num_referencia,
            "talla": t.talla,
            "stock": t.stock
        })
    return resultado

#
