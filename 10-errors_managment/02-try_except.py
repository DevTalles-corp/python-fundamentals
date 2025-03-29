
def divide_numbers():
    try:
        a = int(input("Ingresa el numerador: "))  # a / b
        b = int(input("Ingresa el denominador: "))

        result = a/b
        print(result)
        return result
    except ValueError:
        print("Por favor, ingresa solo números.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    except Exception as error:
        print(type(error))


divide_numbers()
# try

# except
