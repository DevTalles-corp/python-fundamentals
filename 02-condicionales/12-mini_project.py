
# Instrucciones:
# Crearás un programa de evaluación de candidatos potenciales con conocimientos en Python para RH.
# Obtendrás el nombre, años de experiencia y habilidades.

# Evaluarás:
# * Si el candidato sabe Python/Django, tiene +3 años de experiencia: Candidato Optimo.
# * Si el candidato sabe  Python/Django, tiene +1 año de experiencia : Buen candidato.
# * Si el candidato sabe Python/Django: Posible candidato
# * Si el candidato no sabe Python: No optimo, se guardará CV

# Consejo: Ocupa los metodos .split()

name = input("Nombre del candidato: ")
experience = int(input("Años de experiencia: "))
skills = input(
    "Ingrese sus habilidades separadas por comas (ej. Python, Laravel, Golang, Django, etc)").split(",")


evaluate_skills = "Python" in skills or "Django" in skills

result = ""
if evaluate_skills:
    if experience >= 3:
        result = "Candidato optimo"
    elif experience >= 1:
        result = "Buen candidato"
    else:
        result = "Posible candidato"
else:
    result = "No apto, se guardará CV para futuras ofertas"

print(f"El candidato {name} es: {result}")
