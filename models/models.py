from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    productos = relationship("Producto", back_populates="categoria")

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    marca = Column(String)
    num_referencia = Column(String)
    precio = Column(Float)
    tipo = Column(String)
    proveedor = Column(String)
    categoria_id = Column(Integer, ForeignKey("categoria.id"))
    estado = Column(String)

    categoria = relationship("Categoria", back_populates="productos")
    tallas = relationship("TallaProducto", back_populates="producto")

    #TallaProducto
class TallaProducto(Base):
    __tablename__ = "talla_producto"
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("producto.id"))
    talla = Column(String)
    stock = Column(Integer)

    producto = relationship("Producto", back_populates="tallas")

class Rol(Base):
    __tablename__ = "rol"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False, unique=True)
    contraseña = Column(String, nullable=False)
    rol_id = Column(Integer, ForeignKey("rol.id"))
    estado = Column(String)

    rol = relationship("Rol", back_populates="usuarios")

class Venta(Base):
    __tablename__ = "venta"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(String)  # puedes usar DateTime si prefieres
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    usuario = relationship("Usuario")
    detalles = relationship("DetalleVenta", back_populates="venta")

class DetalleVenta(Base):
    __tablename__ = "detalle_venta"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("venta.id"))
    talla_producto_id = Column(Integer, ForeignKey("talla_producto.id"))
    cantidad = Column(Integer)

    venta = relationship("Venta", back_populates="detalles")
    talla_producto = relationship("TallaProducto")
