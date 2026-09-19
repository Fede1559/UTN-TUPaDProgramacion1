nombre = input("ingrese su nombre como cliente: ")
while not nombre.isalpha():
    nombre = input("invalido, solo letras, no numero. Ingrese nuevamente: ")

productos = input("ingrese cantidad de productos a comprar: ")
while not productos.isdigit() or int(productos) <= 0:
    productos = input("debe ser un numero entero positivo: ")
cantidad = int(productos)

# listado de productos
totalsindesc = 0
totalcondes = 0

for i in range(cantidad):
    precio = input(f"precio del producto {i+1}: ")
    while not precio.isdigit():
        precio = input("debe ser un numero entero: ")
    precio = int(precio)

    descuento = input("¿tiene algun descuento? (S/N): ")
    while descuento.lower() not in ("s", "n"):
        descuento = input("respuesta invalida, ingrese S o N: ")

    totalsindesc += precio
    if descuento.lower() == "s":
        preciofinal = precio * 0.9
    else:
        preciofinal = precio
    totalcondes += preciofinal

promedio = totalcondes / cantidad
print(f"total sin descuento: {totalsindesc:.2f}")
print(f"total con descuento: {totalcondes:.2f}")
print(f"ahorro total: {totalsindesc - totalcondes:.2f}")
print(f"promedio por producto: {promedio:.2f}")