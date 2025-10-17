import os 
from dotenv import load_dotenv
import psycopg
from pydantic import BaseModel


load_dotenv()
password = os.getenv("passwords")
# definimos las clases

class cliente(BaseModel):
    nombre: str
    apellido: str

class producto(BaseModel):
    nomPRODUCTOS: str
    precio: float

class carrito:
    def __init__(self):
        self.productos = []

    # agregamos productos al carrito
    def agregar_productos(self, productos1: producto):
        self.productos.append(productos1)

    # get de los productos que agregamos
    def mostrar_productos(self):
        total = sum(p.precio for p in self.productos)
        return {
            "productos": [p.dict() for p in self.productos],
            "total": total
        }

    #eliminar usuario en bd
    
    def eliminar_cliente(self, id_cliente: int):
        conn = psycopg.connect(
            dbname="clienteProducto",
            user="tralalero",
            password= "+passwords",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
        conn.commit()
        cursor.close()
        conn.close()
        return {"mensaje": f"Cliente {id_cliente} eliminado"}
    
    #modificar usuario en bd

    def modificar_cliente(self, id_cliente: int, cliente1: cliente):
        conn = psycopg.connect(
            dbname="clienteProducto",
            user="tralalero",
            password = "passwords",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE cliente SET nombre = %s, apellido = %s WHERE id_cliente = %s",
            (cliente1.nombre, cliente1.apellido, id_cliente)
        )
        conn.commit()
       
        return {"mensaje": f"Cliente {id_cliente} actualizado"}

    # BD de clientes insertar y relacionar
    def baseDeDatos(self, cliente1: cliente, producto1: producto):
        conn = psycopg.connect(
            mibd="clienteProducto",
            usuario="tralalero",
            contraseña= "passwords",
            host="localhost",
            puerto="1234"
        )
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS cliente(id_cliente SERIAL PRIMARY KEY,nombre TEXT,apellido TEXT)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS producto( id_producto SERIAL PRIMARY KEY, nombrePROD TEXT, precio NUMERIC)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS pedido(id_pedido SERIAL PRIMARY KEY,id_cliente INTEGER REFERENCES cliente(id_cliente),id_producto INTEGER REFERENCES producto(id_producto), totalPRECIO NUMERIC)""")
       
        cursor.execute("INSERT INTO cliente (nombre, apellido) VALUES (%s, %s)",(cliente1.nombre, cliente1.apellido))
        cursor.execute("INSERT INTO producto (nombrePROD, precio) VALUES (%s, %s)",(producto1.nomPRODUCTOS, producto1.precio))

# recordatorio PC n°7