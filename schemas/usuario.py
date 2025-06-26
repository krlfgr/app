from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    contraseña: str
    rol_id: int
    estado: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
