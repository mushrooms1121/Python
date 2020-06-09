# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:54:05 2020

@author: mushroom
"""

from Date import Date

class Student():
    def __init__(self,newName,newMonth,newDay,newYear,newScore):
        self.__name = newName
        self.__date = Date(newMonth,newDay,newYear)
        self.__score = newScore
        
    def setName(self,newName):
        self.__name = newName
    def setDate(self,newMonth,newDay,newYear):
        self.__date.setMonth(newMonth)
        self.__date.setDay(newDay)
        self.__date.setYear(newYear)
    def setScore(self,newScore):
        self.__score = newScore
    def getName(self):
        return self.__name
    def getDate(self):
        return self.__date
    def getScore(self):
        return self.__score
    def toString(self):
        print(self.__name,self.__date.toString(),self.__score)