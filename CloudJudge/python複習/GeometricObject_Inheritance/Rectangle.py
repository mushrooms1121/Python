# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:11:24 2020

@author: mushroom
"""

from GeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, newWidth, newHeight, newColor, newFilled):
        self.__width = newWidth
        self.__height = newHeight
        self.setColor(newColor)
        self.setFilled(newFilled)
    def getWidth(self):
        return self.__width
    def setWidth(self, newWidth):
        self.__width = newWidth
    def getHeight(self):
        return self.__height
    def setHeight(self, newHeight):
        self.__height = newHeight
    def getArea(self):
        return self.__height * self.__width
    def getPerimeter(self):
        return 2*(self.__width + self.__height)
