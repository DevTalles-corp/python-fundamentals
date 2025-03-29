
try:
    with open("sinpermisos.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permisos para abrir este archivo")
except Exception as err:
    print(f"Ocurrió un error: {err}")
