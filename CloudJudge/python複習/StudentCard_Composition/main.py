# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:54:02 2020

@author: mushroom
"""

from Student import Student

s1 = Student("John", 6, 1, 1999, 90)
s2 = Student("Marry", 10, 8, 1997, 80)

n = str(input())
m = int(input())
d = int(input())
y = int(input())

s1.setName(n)
s2.setDate(m,d,y)

s1.toString()
s2.toString()