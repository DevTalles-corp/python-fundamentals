
class CoffeMaker:
    def make_coffe(self):
        self.__boil_water()
        self.__mix()
        print("PIP PIP")
        print("Tu café está listo")

    def __boil_water(self):
        print("Hirviendo agua...")

    def __mix(self):
        print("Combinando café y agua...")


coffe_maker = CoffeMaker()
coffe_maker.make_coffe()
