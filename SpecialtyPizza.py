# SpecialtyPizza.py
from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = str(name)
        if size == "S":
            self.price = 12.00
        if size == "M":
            self.price = 14.00
        if size == "L":
            self.price = 16.00
    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\n" + "Size: " + self.size + "\n"+\
               "Name: " + self.name +"\n" + "Price: $" + \
               "{:.2f}".format(self.price) + "\n"

