from proyecto import *

prod1 = Producto("Maruchan", 16, 100)
prod2 = Producto("Coca-Cola 600ml", 18, 150)
prod3 = Producto("Papas Sabritas", 17, 80)
prod4 = Producto("Leche Entera 1L", 26, 60)
prod5 = Producto("Pan Blanco Grande", 45, 40)
prod6 = Producto("Huevo 12 piezas", 38, 30)
prod7 = Producto("Arroz Blanco 1kg", 22, 90)
prod8 = Producto("Frijol Negro 1kg", 35, 75)
prod9 = Producto("Aceite Vegetal 1L", 42, 50)
prod10 = Producto("Azúcar Estándar 1kg", 28, 110)
prod11 = Producto("Café Soluble 100g", 55, 45)
prod12 = Producto("Atún en Agua", 20, 120)
prod13 = Producto("Pasta de Dientes", 32, 65)
prod14 = Producto("Jabón de Barra", 15, 200)
prod15 = Producto("Shampoo 400ml", 60, 35)
prod16 = Producto("Detergente 1kg", 38, 55)
prod17 = Producto("Galletas María", 19, 85)
prod18 = Producto("Refresco de Naranja", 16, 140)
prod19 = Producto("Agua Natural 1.5L", 14, 180)
prod20 = Producto("Servilletas 100pzs", 25, 70)

cat1=Categoria("Alimentos")
lst1=[prod4, prod5, prod6, prod7, prod8]
for a in lst1:
    cat1.agregar_producto(a)
print (cat1.lista_producto)