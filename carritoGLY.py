import sqlite3
from pydantic import baseModel
#definimos las clases

class cliente(baseModel):
            nombre: str
            apellido:str
        
class producto(baseModel):
            nomPRODUCTOS: str
            precio: float

class carrito:
    def __init__(self):
        self.productos = []

    #agregamos prodcutos al carrito
    def agregar_productos(self, productos1:producto):
        self.productos.append(productos1)

    #get de los productos que agregamos
    def mostrar_productos(self):
            total = sum(p.precio for p in self.productos)
            return {
            "productos": [p.dict() for p in self.productos],
            "total": total
        }
    
    #BD de clientes insetar y relacionar
    def baseDeDatos(self, cliente1: cliente, producto1: producto):
            baseDB = sqlite3.connect("baseDeDatos.bd")
            cursor = baseDB.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS cliente(id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, apellido TEXT)")
            cursor.execute("CREATE TABLE IF NOT EXISTS producto(id_producto INTEGER PRIMARY KEY AUTOINCREMENT, nombrePROD TEXT, precio NUMBER)")
            cursor.execute("""CREATE TABLE IF NOT EXISTS pedido(id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,id_cliente INTEGER,id_producto INTEGER,totalPRECIO NUMBER,FOREIGN KEY (id_cliente) REFERENCES 
                       cliente(id_cliente),FOREIGN KEY (id_producto) REFERENCES producto(id_producto))
            """)
            cursor.execute("INSERT INTO cliente (nombre, apellido) VALUES (?, ?)", (cliente1.nombre, cliente1.apellido))
            cursor.execute("INSERT INTO producto (nombrePROD, precio) VALUES (?, ?)", (producto1.nomPRODUCTOS, producto1.precio))
   
    def DropClienProdctoBD(self):
           
            baseDB = sqlite3.connect("baseDeDatos.bd")
            cursor = baseDB.cursor()
            cursor.execute("SELECT cliente.nombre, cliente.apellido, producto.nombrePROD, producto.precio FROM pedido JOIN cliente ON pedido.id_cliente = cliente.id_cliente JOIN producto ON pedido.id_producto = producto.id_producto")
           
        #recordatorio PC n°7
