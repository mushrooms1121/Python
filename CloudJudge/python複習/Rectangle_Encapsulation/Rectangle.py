# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 01:13:30 2020

@author: mushroom
"""

class Rectangle:
   def __init__(self, newWidth , newLength):
       self.__width = newWidth
       self.__length = newLength
   def setLength(self, newLength):
        self.__length = newLength
   def setWidth(self, newWidth):
        self.__width = newWidth
   def getLength(self):
       return self.__length
   def getWidth(self):
       return self.__width
   def getArea(self):
        return self.__length * self.__width
   def getPerimeter(self):
       return 2 * (self.__width + self.__length)