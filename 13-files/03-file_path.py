
# Relative Path
with open('../Archivos/archivo.txt', mode="r") as my_file:
    print(my_file.readlines())

# Absolute Path
# Aquí meti la ruta en una variable para que no te de error la extensión
absolute_path = '/Users/ricardocuellar/Desktop/python/Archivos/archivo.txt'
with open(absolute_path, mode="r") as my_file:
    print(my_file.readlines())
