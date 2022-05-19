'''
AnimalLab.py
'''
class AnimalLab:
    def __init__(self, species = None, weight = None, age = None, name = None):
            self.species = species
            self.weight = weight
            self.age = age
            self.name = name
            if self.species != None:    
                self.species = str(species).upper()
            if self.weight != None:
                self.weight = float(weight)
            if self.age != None:
                self.age = int(age)
            if self.name != None:
                self.name = str(name).upper()
        
    def setSpecies(self, species):
        self.species = str(species).upper()
    def setWeight(self, weight):
        self.weight = float(weight)
    def setAge(self, age):
        self.age = int(age)
    def setName(self, name):
        self.name = str(name).upper()

    def toString(self):
        return ("Species: {}, Name: {}, Age: {}, Weight: {}" \
              .format(self.species, self.name, self.age, self.weight))

