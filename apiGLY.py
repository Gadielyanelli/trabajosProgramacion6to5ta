from fastapi import fastAPI
from carritoGLY import carrito
from carritoGLY import producto
from carritoGLY import cliente

cursor_Carrito = carrito()
app = fastAPI(title=("carrito de compra"))


#get productos
@app.get("/carrito")
def ver_PRODUCTO():
    return cursor_Carrito.mostrar_productos()
#agregar productos a DB

@app.postDB("/guardar")
def guardar_PRODUCTO(cliente1:cliente, prodcuto1:producto):
    cursor_Carrito.baseDeDatos(cliente1,prodcuto1)
    return {"se guardo al pendejo con el producto"}

#agregar a carrito los productos
@app.post("/agregarProducto")
def agregar_Producto(producto):
    cursor_Carrito.agregar_productos(producto)
    return (f"{producto}agregado a la lista.")




#esta flaca la API