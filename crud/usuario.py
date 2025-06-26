from sqlalchemy.orm import Session
from models.models import Usuario
from schemas.usuario import UsuarioCreate

def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo = Usuario(**usuario.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()
