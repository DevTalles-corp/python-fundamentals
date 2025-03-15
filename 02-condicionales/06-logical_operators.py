
# Evaluar condiciones

# and (todos los valores sean verdaderos)
# print(True and True)  # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False)  # False

# # or (al menos uno debe ser verdadero)
# print(True or True)  # True
# print(True or False)  # True
# print(False or True)  # True
# print(False or False)  # False

# # not (negar)
# print(not True)  # False
# print(not False)  # True


# and
age = 25
licensed = True

if age >= 18 and licensed:
    print("Puedes conducir")

# or
is_student = False
membership = True

if is_student or membership:
    print("Obtienes un descuento especial")

# not
is_admin = False

if not is_admin:
    print("Acceso denegado")
