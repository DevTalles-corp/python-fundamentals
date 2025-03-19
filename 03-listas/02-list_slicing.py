
shopping_cart = [
    'Camisas',
    'Tenis',
    'Calcetas',
    'Pantalones'
]

# [Inicio : fin]
# new_list = shopping_cart[1:3]

# new_list[0] = 'Zapatos'
# new_list[1] = 'Collar'
# shopping_cart[0] = 'Playeras'

# print(new_list)  # Crea una lista nueva
# print(shopping_cart)

# Copiar una lista

new_cart = shopping_cart[:]
new_cart[0] = 'Playeras'
shopping_cart[1] = 'Zapatos'
print(shopping_cart)
print(new_cart)
