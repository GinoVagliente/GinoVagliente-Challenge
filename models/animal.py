class Animal:
    def __init__(self, species, name, numLegs, gender):
        self.species = species
        self.name = name
        self.numLegs = numLegs
        self.gender = gender
    

    #Has the ability to print out a description of the Animal using the class level information
    def description(self):
        return f"{self.name} is a {self.species} with {self.numLegs} legs and is {self.gender}."