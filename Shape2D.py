'''
Shape2D.py
'''

class Shape2D:

    def __init__(self, color = None):
        self.color = color
        if self.color != None:
            self.color = str(color)

    def setColor(self, color):
        self.color = str(color)

    def getColor(self):
        return self.color

    def getShapeProperties(self):
        return ("Shape: N/A, Color: {}" \
              .format(self.color))
