# PizzaOrder.py
from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder(Pizza):
    def __init__(self, time):
        self.time = int(time)
        self.pizzas = []
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = int(time)
    def addPizza(self, pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        string = ""
        for x in self.pizzas:
            if x == self.pizzas[-1]:
                string += x.getPizzaDetails() + "\n"
                string += "----"
            else:
                string += x.getPizzaDetails() + "\n"
                string += "----\n"   
        total_price = 0.0
        for x in self.pizzas:
            total_price += x.getPrice()
        return "******\nOrder Time: {}\n{}\nTOTAL ORDER PRICE: ${:.2f}\n******\n"\
               .format(self.time, string, total_price)
