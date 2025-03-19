
#  letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#  numeros = "0123456789"
#  simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
# caracteres = letras + numeros + simbolos
# Formula simple: (item * 7 + 3) % len(caracteres)

# Entrada: 8
# Salida : &D^#23SN

import string
import random


def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []

    password = ''.join(random.choice(chars) for _ in range(length))

    return password


length = int(input("¿Cuántos caracteres quieres en tu contraseña? "))
print("Tu contraseña segura es: ", password_generator(length))
