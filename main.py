from models.animal import Animal
from models.zoo import Zoo
from models.species.giraffe import Giraffe
from models.species.crocodile import Crocodile
from models.species.giantTortoise import GiantTortoise


newZoo = Zoo("ZoologicoCordoba", "Villa Maria", "13:00")
newAnimal = Animal("Felino", "Gatito", "4", "Male")

print(newZoo.AnimalsCount())

newZoo.addAnimal(newAnimal)

print(newZoo.AnimalsCount()) 

#newZoo.removeAnimal(newAnimal)
newZoo.printAnimalsAll()

newZoo.todayPrice("Tuesday")

giraffe1 = Giraffe("Girafa", "Male", 5.8)
giraffe2 = Giraffe("Girafo", "Female", 4.6)

giraffe1.compareHeight(giraffe2)

croc = Crocodile("Cocodrilo", "Female", 75, ["fish", "chicken", "meat"])

print(croc.favFoods())

tortoise = GiantTortoise("Tortugita", "Male" , 60)
tortoise.ageDescription()



