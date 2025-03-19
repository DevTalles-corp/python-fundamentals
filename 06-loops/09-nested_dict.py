
nested_dict = {
    "Persona1": {"Nombre": "Ricardo", "edad": 29, "ciudad": "Ciudad de México"},
    "Persona2": {"Nombre": "Brenda", "edad": 26, "ciudad": "Huejutla de Reyes"},
    "Persona3": {"Nombre": "Estela", "edad": 50, "ciudad": "Cancún"}
}


for key, value in nested_dict.items():
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f" {sub_key}: {sub_value}")
