from fastapi import FastAPI
from carritoGLY import carrito, producto, cliente

app = FastAPI(title="carrito de compra")
cursor_Carrito = carrito()

@app.get("/carrito")
def ver_productos():
    return cursor_Carrito.mostrar_productos()

@app.post("/guardar")
def guardar_producto(cliente1: cliente, producto1: producto):
    cursor_Carrito.baseDeDatos(cliente1, producto1)
    return {"mensaje": "se guardo"}

@app.post("/agregarProducto")
def agregar_producto(producto1: producto):
    cursor_Carrito.agregar_productos(producto1)
    return {"mensaje": f"Producto {producto1.nomPRODUCTOS} agregadd"}

@app.delete("/eliminar/{id_cliente}")
def eliminar_cliente(id_cliente: int):
    return cursor_Carrito.eliminar_cliente(id_cliente)

@app.put("/modificar/{id_cliente}")
def modificar_cliente(id_cliente: int, cliente1: cliente):
    return cursor_Carrito.modificar_cliente(id_cliente, cliente1)