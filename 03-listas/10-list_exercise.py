
# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = input("Elige una opción (1-6): ")

if option == "1":
    product = input("Ingresa un nombre de producto: ")
    if product not in shopping_cart:
        shopping_cart.append(product)
        print("Producto agregado")
    else:
        print("El producto ya se encuentra en tu carrito")
elif option == "2":
    product = input("Ingresa un nombre de producto: ")
    if product in shopping_cart:
        shopping_cart.remove(product)
        print("Producto eliminado")
    else:
        print("El producto no está en la lista")
elif option == "3":
    if len(shopping_cart) > 0:
        print("Lista de compras: ")
        shopping_cart.sort()
        print(shopping_cart)
    else:
        print("La lista esta vacía")
elif option == "4":
    product = input("Ingresa un nombre de producto a buscar: ")
    if product in shopping_cart:
        print(f"{product} esta en la lista de compras")
    else:
        print("Producto no encontrado")
elif option == "5":
    print("Total de productos: ", len(shopping_cart))
elif option == "6":
    shopping_cart.clear()
    print("Lista vacia")
else:
    print("Opción no válida.")


print(shopping_cart)
