
students = {
    "Ana": [8, 7, 9],
    "Luis": [6, 5, 7],
    "Sofía": [10, 9, 10]
}

# Agregar nuevo estudiante
# Sacar el promedio de un estudiante existente
# El promedio del estudiante nuevo

students["Ricardo"] = [10, 7, 9]

name = "Ricardo"
if name in students:
    student_grades = students[name]
    total_grade = (student_grades[0]+student_grades[1]+student_grades[2]) / 3

    if total_grade >= 6.0:
        print(f"{name} aprobó con un promedio de: {total_grade:.2f}")
    else:
        print(f"{name} reprobó con un promedio de: {total_grade:.2f}")

else:
    print("El estudiante no está registrado.")
