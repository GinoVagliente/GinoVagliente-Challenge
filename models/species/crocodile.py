from models.animal import Animal

class Crocodile(Animal):
    def __init__(self, name, gender, numTeeth, favoriteFoods):
        super().__init__("Crocodile", name, 4, gender)
        self.numTeeth = numTeeth
        self.favoriteFoods = [favoriteFoods]

    def favFoods(self):
        return self.favoriteFoods
