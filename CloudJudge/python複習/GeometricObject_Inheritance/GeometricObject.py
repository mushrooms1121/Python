class GeometricObject():
    def __init__(self,newColor,newFilled):
        self.__color = newColor
        self.__filled = newFilled
    def getColor(self):
        return self.__color
    def setColor(self,newColor):
        self.__color = newColor
    def isFilled(self):
        return self.__filled
    def setFilled(self,newFilled):
        self.__filled = newFilled
    def __str__(self):
        print(self.__color,self.__filled)
