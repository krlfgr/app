from fastapi import FastAPI
from database import Base, engine
from routers import producto, talla_producto, categoria, rol, usuario, venta, informes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(producto.router)
app.include_router(producto.router)
app.include_router(talla_producto.router)
app.include_router(categoria.router)
app.include_router(rol.router)
app.include_router(usuario.router)
app.include_router(venta.router)
app.include_router(informes.router)

@app.get("/")
def root():
    return {"msg": "API para empresa de calzado funcionando"}
