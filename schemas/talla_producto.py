from pydantic import BaseModel

class TallaProductoBase(BaseModel):
    producto_id: int
    talla: str
    stock: int

class TallaProductoCreate(TallaProductoBase):
    pass

class TallaProductoOut(TallaProductoBase):
    id: int

    class Config:
        from_attributes = True
