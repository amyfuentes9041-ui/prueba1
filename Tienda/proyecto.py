class Producto:
    def __init__(self, nombre, precio, stok):
        self.nombre = nombre
        self.precio= precio
        self.stock = stok
    
    def aplicar_descuento (self, porcentaje):  
        self.precio *= (1-porcentaje)
        print (f"El nuevo precio es {self.precio}")

    def actualizar_stok (self, cantidad):
        if (self.stock+cantidad)<0:
            print ("No puedes tener stock negativo")
        else:
            self.stock+=cantidad
            print (f"La nueva cantidad es {self.stock}")

class Categoria:
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.lista_producto = []

    def agregar_producto (self, producto):
        self.lista_producto.append(producto)
        print ( f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma=0
        for b in self.lista_producto:
            suma +=b.precio
        print (f"El valor total de la categoria es {suma}")

class Pedido:
    def __init__(self, cliente, productos_comprados, estado):
        self.cliente = cliente 
        self.productos_comprados = []

    def calcular_total (self):
        suma = 0 
        for b in self.productos_comprados:
            suma +=b.precio
        
