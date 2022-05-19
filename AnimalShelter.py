'''
AnimalShelter.py
'''
from Animal import Animal

class AnimalShelter:

    def __init__(self):
        self.shelter = {}
        
    def addAnimal(self, animal):
        if animal.species in self.shelter:
            self.shelter[animal.species].append(animal)
        else:
            self.shelter[animal.species] = [animal]

    def removeAnimal(self, animal):
            if self.doesAnimalExist(animal) == True:
                self.shelter[animal.species].remove(animal)

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        specstr = ''
        if species not in self.shelter:
            return specstr
        if species in self.shelter:
            for y in self.shelter[species]:
                specstr += y.toString() + '\n'
            return specstr[:-1]
            
    def  doesAnimalExist(self, animal):
        if animal.species in self.shelter:
            if animal in self.shelter[animal.species]:
                return True
            else:
                return False
        else:
            return False

