from typing import Generator
import os
from dotenv import load_dotenv
import psycopg
from pydantic import BaseModel


load_dotenv()
password = os.getenv("passwords")

url = f"postgresql://postgres.slcwqkacolixtbssmhdx:{password}@aws-1-us-east-2.pooler.supabase.com:6543/postgres"


def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")

    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()
nombrecliente = ""
# Definimos las clases
class cliente(BaseModel):
    nombre: str
    apellido: str

class producto(BaseModel):
    nomPRODUCTOS: str
    precio: float

class pedido(BaseModel):
    id_pedido: int
    id_producto: int
    id_cliente: int


class carrito:

    def eliminarCliente(self, id_cliente: int, cursor):
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
        return {"mensaje": f"Cliente {id_cliente} eliminado"}

    def eliminarProducto(self, id_producto: int, cursor): 
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        return {"mensaje": f" Producto {id_producto} eliminado"}

    def eliminarPedido(self, id_pedido: int, cursor):
        cursor.execute("DELETE FROM pedido WHERE id_pedido = %s", (id_pedido,))

        return {"mensaje": f"pedido {id_pedido} eliminado"}

    def mostrarProductos(self, cursor):
        cursor.execute("SELECT * FROM productos")
        for item in cursor:
            return item
        

    def mostrarCliente(self, cursor):
        cursor.execute("SELECT * FROM cliente")
        for item in cursor:
            return item


    def insertarPedido(self, pedido1: pedido, cursor):
        cursor.execute("INSERT INTO pedido (id_pedido, id_cliente, id_producto) VALUES (%s, %s, %s)", (pedido1.id_pedido, pedido1.id_cliente, pedido1.id_producto))
        return {"mensaje": "insertado"}
    
    def mostrarPedido(self, cursor):
        cursor.execute("SELECT * FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente")
        for item in cursor:
            return item
    

    def modificarCliente(self, id_cliente: int, cliente1: cliente, cursor):
        cursor.execute(
            "UPDATE cliente SET nombre = %s, apellido = %s WHERE id_cliente = %s",
            (cliente1.nombre, cliente1.apellido, id_cliente))
        

        return {"mensaje": f"Cliente {id_cliente} actualizado"}

    def agregarProducto(self, producto1: producto, cursor):
        cursor.execute(+-
                       
            "INSERT INTO productos (nombre, precio) VALUES (%s, %s)",
            (producto1.nomPRODUCTOS, producto1.precio)
        )
    def agregarCliente(self, cliente1: cliente, cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre, apellido) VALUES (%s, %s)",
            (cliente1.nombre, cliente1.apellido)
        )


        return {"mensaje": f"Producto '{cliente1.nombre}' agregado a la base de datos"}

    def modificarProducto(self, id_producto: int, producto1: producto, cursor):
        cursor.execute("UPDATE productos SET nombre = %s, precio = %s WHERE id_producto = %s",
            (producto1.nomPRODUCTOS,producto1.precio,id_producto))


        return {"mensaje": f"Cliente {id_producto} actualizado"}
#MM, APAC,  MCMP,  ECEP