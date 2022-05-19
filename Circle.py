'''
Circle.py
'''
from Shape2D import Shape2D

class Circle(Shape2D):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def computeArea(self):
        return 3.14159 * (self.radius **2)

    def computePerimeter(self):
        return 2*3.14159*self.radius

    def getShapeProperties(self):
        return ("Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}" \
              .format(self.color, self.getRadius(), self.computeArea(), self.computePerimeter()))


