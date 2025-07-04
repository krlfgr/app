from pydantic import BaseModel

class RolBase(BaseModel):
    nombre: str

class RolCreate(RolBase):
    pass

class RolOut(RolBase):
    id: int

    class Config:
        from_attributes = True
