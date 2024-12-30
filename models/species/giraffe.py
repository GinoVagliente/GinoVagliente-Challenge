from models.animal import Animal

class Giraffe(Animal):
    def __init__(self, name, gender, height):
        super().__init__('Giraffe', name, 4, gender)
        self.height = height

    def compareHeight(self, other_giraffe):
        if not isinstance(other_giraffe, Giraffe):
            print("Comparison is only valid between Giraffes.")
            return
        
        if self.height > other_giraffe.height:
            print(f"{self.name} is taller than {other_giraffe.name}.")
        elif self.height < other_giraffe.height:
            print(f"{self.name} is shorter than {other_giraffe.name}.")
        else:
            print(f"{self.name} and {other_giraffe.name} are the same height.")
