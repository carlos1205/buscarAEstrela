class Room:
    def __init__(self, label, lengthX, lengthY):
        self.__label = label
        self.__lengthX = lengthX
        self.__lengthY = lengthY
        self.__doors = []
    
    def setDoors(self, doors):
        self.__doors = doors

    def addDoor(self, door):
        self.__doors.append(door)

    def getLabel(self):
        return self.__label
    
    def getDoors(self):
        return self.__doors

    def getArea(self):
        return self.__lengthX * self.__lengthY