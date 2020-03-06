#Name: Jayson Sandhu
#Student ID: 100659589
#Question 1

import math

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getArea(self):
        return 'Error:  Cannot get area of abstract shape'
    def getPerimeter(self):
        return 'Error:  Cannot get perimeter of abstract shape'
    
class Rectangle(Shape):
    def __init__(self, width, length):
        self.x = width
        self.y = length
    def getLength(self):
        return self.y
    def getWidth(self):
        return self.x   
    def getArea(self):
        return self.x * self.y
    def getPerimeter(self):
        return self.x * 2 + self.y * 2
    
class Circle(Shape):
    def __init__(self,radius):
        self.x = radius
    def getRadius(self):
        return self.radius
    def getArea(self):
        return math.pi * pow(self.x,2)
    def getPerimeter(self):
        return 2 * math.pi * self.x

def main():
   if __name__ == "__main__":
       main()