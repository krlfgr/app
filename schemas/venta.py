from pydantic import BaseModel
from typing import List

class DetalleVentaBase(BaseModel):
    talla_producto_id: int
    cantidad: int

class DetalleVentaCreate(DetalleVentaBase):
    pass

class DetalleVentaOut(DetalleVentaBase):
    id: int
    class Config:
        from_attributes = True

class VentaBase(BaseModel):
    fecha: str
    usuario_id: int

class VentaCreate(VentaBase):
    detalles: List[DetalleVentaCreate]

class VentaOut(VentaBase):
    id: int
    detalles: List[DetalleVentaOut]

    class Config:
        from_attributes = True
