
class Animal:
    def make_sound(self):
        print("Sonido de animal")


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow Meow!")


def make_noise(animal):
    if isinstance(animal, Animal):
        animal.make_sound()
    else:
        print("Esto no es un animal")


make_noise(Dog())
make_noise(Cat())
make_noise("Hola Mundo")
