from sqlalchemy.orm import Session
from models.models import Venta, DetalleVenta, TallaProducto
from schemas.venta import VentaCreate

def crear_venta(db: Session, venta: VentaCreate):
    nueva_venta = Venta(fecha=venta.fecha, usuario_id=venta.usuario_id)
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)

    for detalle in venta.detalles:
        talla = db.query(TallaProducto).filter(TallaProducto.id == detalle.talla_producto_id).first()
        if not talla:
            raise ValueError(f"TallaProducto ID {detalle.talla_producto_id} no existe.")
        if talla.stock < detalle.cantidad:
            raise ValueError(f"No hay suficiente stock para talla {detalle.talla_producto_id}.")
        
        talla.stock -= detalle.cantidad  # Descontar stock

        detalle_venta = DetalleVenta(
            venta_id=nueva_venta.id,
            talla_producto_id=detalle.talla_producto_id,
            cantidad=detalle.cantidad
        )
        db.add(detalle_venta)

    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

def obtener_ventas(db: Session):
    return db.query(Venta).all()
