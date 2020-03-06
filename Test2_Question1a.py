#Name: Jayson Sandhu
#Student ID: 100659589
#Question 1a

import math

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def getLength(self):
        return self.length
    def getWidth(self):
        return self.width
    def getArea(self):
        return self.width * self.length
    def getPerimeter(self):
        return self.width * 2 + self.length * 2

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def getArea(self):
        return math.pi * pow(self.radius,2)
    def getPerimeter(self):
        return 2 * math.pi * self.radius

def main():
    if __name__ == "__main__":
        main()