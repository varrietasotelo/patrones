import random


class PetShop:

    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print ("Este es un Magnifico", pet)
        print ("El dice", pet.speak())
        print ("El come", self.pet_factory.get_food())

# Lo que el factory hace:


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Perro"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Gato"


# Clases
class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Comida de Perro"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Comida de gato"

def get_factory():
    return random.choice([DogFactory, CatFactory])()

# Test de la fabrica
shop = PetShop()
for i in range(2):
    shop.pet_factory = get_factory()
    shop.show_pet()
