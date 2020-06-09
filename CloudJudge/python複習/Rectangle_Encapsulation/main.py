# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 01:13:36 2020

@author: mushroom
"""

from Rectangle import Rectangle

w1 = int(input())
w2 = int(input())
l1 = int(input())
l2 = int(input())

r1 = Rectangle(w1, l1)
r2 = Rectangle(w2, l2)

print(r1.getArea(), r1.getPerimeter())
print(r2.getArea(), r2.getPerimeter())

r2.setLength(50)
r2.setWidth(25)

print(r2.getArea(), r2.getPerimeter())