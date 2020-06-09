# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:11:35 2020

@author: mushroom
"""

from GeometricObject import GeometricObject
from Circle import Circle
from Rectangle import Rectangle

cr = int(input())
rw = int(input())
rh = int(input())
cc = str(input())
cf = bool(input())
rc = str(input())
rf = bool(input())

c = Circle(cr, cc, cf)
r = Rectangle(rw, rh, rc, rf)

print("Circle:")
print("Radius is {0}\nDiameter is {1}\nArea is {2}\nPerimeter is {3}"\
      .format(c.getRadius(),c.getDiameter(), c.getArea(), c.getPerimeter()))
print("color: %s and filled: %s"%(c.getColor(), c.isFilled()))

print("\nRectangle:")
print("Width is {0}\nHeight is {1}\nArea is {2}\nPerimeter is {3}\ncolor: {4} and filled: {5}"\
      .format(r.getWidth(), r.getHeight(), r.getArea(), r.getPerimeter(), r.getColor(), r.isFilled()))
