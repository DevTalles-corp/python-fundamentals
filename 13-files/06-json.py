
import json

user = {'nomber': 'Ricardo', 'edad': 29, 'activo': True}

with open("datos.json", "w") as file:
    json.dump(user, file, indent=4)

with open("datos.json", "r") as file:
    data_read = json.load(file)
    print(data_read)
