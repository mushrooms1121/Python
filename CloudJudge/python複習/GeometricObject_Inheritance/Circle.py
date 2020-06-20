import math
from GeometricObject import GeometricObject

class Circle(GeometricObject):
    def __init__(self,newRadius,newColor,newFilled):
        self.__radius = newRadius
        self.setColor(newColor)
        self.setFilled(newFilled)
    def getRadius(self):
        return self.__radius
    def setRadius(self,newRadius):
        self.__radius = newRadius
    def getArea(self): #面積
        return pow(self.__radius,2)*math.pi
    def getDiameter(self): #直徑
        return self.__radius*2
    def getPerimeter(self): #周長
        return self.__radius*2*math.pi
