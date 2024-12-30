class Zoo:
    def __init__(self, name, city, openingHours):
        self.name = name
        self.city = city
        self.openingHours = openingHours
        self.animals = []
        self.admissionPrice = {
        "Monday": 19.99,
        "Tuesday": 19.99,
        "Wednesday": 9.99,
        "Thursday" : 19.99,
        "Friday" : 19.99,
        "Saturday" : 25.99,
        "Sunday" : 25.99
        }

#Ability to add an Animal to the Zoo
    def addAnimal(self, newAnimal):
        self.animals.append(newAnimal)

# Ability to remove an Animal from the Zoo
    def removeAnimal(self, oldAnimal):
        if oldAnimal in self.animals:
            self.animals.remove(oldAnimal)

# Ability to print out how many Animals are currently in the zoo
    def AnimalsCount(self):
        return len(self.animals)
    
#Ability to print out descriptions of all the Animals that currently live in the zoo    
    def printAnimalsAll(self):
        for animal in self.animals:
            print(animal.description())

#Ability to determine, depending on the current day of the week, the current Admission Price.
    def todayPrice(self, day):
        if day in self.admissionPrice:
            print(f"The admission price for {day} is: {self.admissionPrice[day]}")
        else:
            print("Invalid day, no price found.")