__author__ = 'aramu'


class Shape:

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "str = Shape"

    def myshape(self):
        print("Base shape")
        print("my color is " + self.color)

class Triangle(Shape):

    def __init__(self, color):
        self.color = color

    def color_function(self):
        print(self.color)

def hello():
    pass

class LoopError(Exception):
    pass
