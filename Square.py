'''
Square.py
'''
from Shape2D import Shape2D

class Square(Shape2D):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        return self.side **2

    def computePerimeter(self):
        return 4*self.side

    def getShapeProperties(self):
        return ("Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}" \
              .format(self.color, self.getSide(), self.computeArea(), self.computePerimeter()))

