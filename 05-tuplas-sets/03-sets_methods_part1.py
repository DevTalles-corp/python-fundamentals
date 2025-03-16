
# Conjuntos

# .add()
my_set = {1, 2, 3}
my_set.add(6)
my_set.add(3)
my_set.add(5)
print(my_set)

# .remove() Elimina un elemento, pero da error sino existe
my_set.remove(2)
my_set.remove(6)
print(my_set)

# .discard() No marca error si no existe
my_set.discard(3)
my_set.discard(3)
my_set.discard(7)

print(my_set)

# .pop() Elimina un elemento al azar y lo devuelve

print(my_set.pop())
print(my_set)
