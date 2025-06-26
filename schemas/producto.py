from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    marca: str
    num_referencia: str
    precio: float
    tipo: str
    proveedor: str
    categoria_id: int
    estado: str

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True
