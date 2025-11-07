from fastapi import FastAPI, Depends
from carritoGLY import carrito, producto, cliente,  getCursor, psycopg, pedido


app = FastAPI(title="carrito de compra")
cursor_Carrito = carrito()

@app.get("/productos")
def ver_productos(cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.mostrarProductos(cursor)

@app.get("/pedido")
def ver_pedido(cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.mostrarPedido(cursor)

@app.get("/Cliente")
def ver_cliente(cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.mostrarCliente(cursor)


@app.get("/pedidos")
def ver_pedidos(cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.mostrarPedido(cursor)

@app.post("/insertarPedido")
def insertarElPedido(pedido1: pedido, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.insertarPedido(pedido1,cursor)

@app.post("/agregarCliente")
def agregar_Cliente(cliente: cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.agregarCliente(cliente, cursor)

@app.post("/agregarProducto")
def agregar_producto(producto1: producto, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.agregarProducto(producto1, cursor)



@app.delete("/eliminarCliente/{id_cliente}")
def eliminar_cliente(id_cliente: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.eliminarCliente(id_cliente, cursor)

@app.delete("/eliminarProducto/{id_producto}")
def eliminar_producto(id_producto: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.eliminarProducto(id_producto, cursor)

@app.delete("/eliminarPedido/{id_pedido}")
def eliminar_pedido(id_pedido: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.eliminarPedido(id_pedido, cursor)

@app.put("/modificarCliente/{id_cliente}")
def modificar_cliente(id_cliente: int, cliente1: cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.modificarCliente(id_cliente, cliente1, cursor)


@app.put("/modificarProducto/{id_producto}")
def modificar_producto(id_producto: int, producto1: producto, cursor: psycopg.Cursor = Depends(getCursor)):
    return cursor_Carrito.modificarProducto(id_producto, producto1, cursor)