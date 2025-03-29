
class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} está durmiendo")


class Dog(Animal):
    def dog_sound(self):
        print(f"{self.name} dice: Guau!")


class Cat(Animal):
    def cat_sound(self):
        print(f"{self.name} dice: Miau!")


firulais = Dog("firulais")
firulais.sleep()
firulais.dog_sound()

malva = Cat("Malva")
malva.sleep()
malva.cat_sound()
