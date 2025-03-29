
class InvalidAgeError(Exception):
    def __init__(self, age, message="La edad debe ser mayor o igual a 18."):
        self.age = age
        self.message = message
        super().__init__(self.message)


class InvalidEmail(Exception):
    def __init__(self, email, message="El correo electrónico no es válido."):
        self.email = email
        self.message = message
        super().__init__(self.message)


def register_user(name, age, email):
    if age < 18:
        raise InvalidAgeError(age)

    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmail(email)

    print(f"Usuario {name} registrado con la edad {age} y el correo {email}")


try:
    register_user("Ricardo", 25, "ricardo@correo.com")
except InvalidAgeError as e:
    print(f"Error: {e}")
except InvalidEmail as e:
    print(f"Error: {e}")
