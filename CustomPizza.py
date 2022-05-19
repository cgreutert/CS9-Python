# CustomPizza
from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if size == "S":
            self.price = 8.00
        if size == "M":
            self.price = 10.00
        if size == "L":
            self.price = 12.00
    def addTopping(self, topping):
        self.toppings.append("\t+ {}".format(topping))
        if (self.size == "S")==True:
            self.price += 0.50
        elif (self.size == "M")==True:
            self.price += 0.75
        elif (self.size == "L")==True:
            self.price += 1.00
    def getPizzaDetails(self):
        if len(self.toppings) == 0:
            return "CUSTOM PIZZA\n" + "Size: " + self.size + "\n"+\
               "Toppings:\n" + "Price: $" + \
               "{:.2f}".format(self.price) + "\n"
        else:
            return "CUSTOM PIZZA\n" + "Size: " + self.size + "\n"+\
               "Toppings:\n" + "\n".join(map(str, self.toppings)) +"\n" + "Price: $" + \
               "{:.2f}".format(self.price) + "\n"
