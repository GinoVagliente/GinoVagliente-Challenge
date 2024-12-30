from models.animal import Animal

class GiantTortoise(Animal):
    def __init__(self, name, gender, age):
        super().__init__("Giant Tortoise", name, 4, gender)
        self.age = age

    def ageDescription(self):
        if(self.age < 50):
            return print("young")
        elif(self.age > 50 and self.age < 100):
            return print("middle-aged")
        else:
            return print("old")
