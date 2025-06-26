from sqlalchemy.orm import Session
from models.models import Rol
from schemas.rol import RolCreate

def crear_rol(db: Session, rol: RolCreate):
    nuevo = Rol(**rol.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_roles(db: Session):
    return db.query(Rol).all()
