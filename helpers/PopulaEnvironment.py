from environment.Environment import Environment
from environment.Room import Room
from environment.Door import Door

class PopulaEnvironment:
    def __init__(self):
        self.__rooms = {}

    def make(self):
        self.createRooms()
        self.createDoors()
        return self.createEnvironment()

    def createRooms(self):
        # x < 8
        # y < 7
        self.__rooms.update({'A': {'room': Room('A', 2, 1),'coordinates': {'x':1 ,'y': 7}}})
        self.__rooms.update({'B': {'room': Room('B', 1, 2),'coordinates': {'x':1 ,'y': 5}}})
        self.__rooms.update({'C': {'room': Room('C', 1, 2),'coordinates': {'x':2 ,'y': 5}}})
        self.__rooms.update({'D': {'room': Room('D', 2, 1),'coordinates': {'x':1 ,'y': 4}}})
        self.__rooms.update({'E': {'room': Room('E', 2, 2),'coordinates': {'x':1 ,'y': 2}}})
        self.__rooms.update({'F': {'room': Room('F', 2, 1),'coordinates': {'x':1 ,'y': 1}}})
        self.__rooms.update({'G': {'room': Room('G', 1, 2),'coordinates': {'x':3 ,'y': 6}}})
        self.__rooms.update({'H': {'room': Room('H', 2, 1),'coordinates': {'x':3 ,'y': 5}}})
        self.__rooms.update({'I': {'room': Room('I', 1, 2),'coordinates': {'x':3 ,'y': 3}}})
        self.__rooms.update({'J': {'room': Room('J', 1, 2),'coordinates': {'x':3 ,'y': 1}}})
        self.__rooms.update({'K': {'room': Room('K', 1, 2),'coordinates': {'x':4 ,'y': 6}}})
        self.__rooms.update({'L': {'room': Room('L', 2, 2),'coordinates': {'x':4 ,'y': 3}}})
        self.__rooms.update({'M': {'room': Room('M', 2, 2),'coordinates': {'x':4 ,'y': 1}}})
        self.__rooms.update({'N': {'room': Room('N', 2, 2),'coordinates': {'x':5 ,'y': 6}}})
        self.__rooms.update({'O': {'room': Room('O', 2, 1),'coordinates': {'x':5 ,'y': 5}}})
        self.__rooms.update({'P': {'room': Room('P', 1, 4),'coordinates': {'x':6 ,'y': 1}}})
        self.__rooms.update({'Q': {'room': Room('Q', 2, 2),'coordinates': {'x':7 ,'y': 6}}})
        self.__rooms.update({'R': {'room': Room('R', 2, 1),'coordinates': {'x':7 ,'y': 5}}})
        self.__rooms.update({'S': {'room': Room('S', 2, 1),'coordinates': {'x':7 ,'y': 4}}})
        self.__rooms.update({'T': {'room': Room('T', 2, 2),'coordinates': {'x':7 ,'y': 2}}})
        self.__rooms.update({'U': {'room': Room('U', 2, 1),'coordinates': {'x':7 ,'y': 1}}})

    def createDoors(self):
        #Portas sala A
        self.__rooms.get('A').get('room').addDoor(Door(self.__rooms.get('C').get('room')))
        #Portas sala B
        self.__rooms.get('B').get('room').addDoor(Door(self.__rooms.get('C').get('room')))
        self.__rooms.get('B').get('room').addDoor(Door(self.__rooms.get('D').get('room')))
        #Portas sala C
        self.__rooms.get('C').get('room').addDoor(Door(self.__rooms.get('A').get('room')))
        self.__rooms.get('C').get('room').addDoor(Door(self.__rooms.get('B').get('room')))
        self.__rooms.get('C').get('room').addDoor(Door(self.__rooms.get('G').get('room')))
        #Portas sala D
        self.__rooms.get('D').get('room').addDoor(Door(self.__rooms.get('B').get('room')))
        self.__rooms.get('D').get('room').addDoor(Door(self.__rooms.get('E').get('room')))
        #Portas sala E
        self.__rooms.get('E').get('room').addDoor(Door(self.__rooms.get('D').get('room')))
        self.__rooms.get('E').get('room').addDoor(Door(self.__rooms.get('F').get('room')))
        #Portas sala F
        self.__rooms.get('F').get('room').addDoor(Door(self.__rooms.get('E').get('room')))
        self.__rooms.get('F').get('room').addDoor(Door(self.__rooms.get('J').get('room')))
        #Portas sala G
        self.__rooms.get('G').get('room').addDoor(Door(self.__rooms.get('C').get('room')))
        self.__rooms.get('G').get('room').addDoor(Door(self.__rooms.get('H').get('room')))
        self.__rooms.get('G').get('room').addDoor(Door(self.__rooms.get('K').get('room')))
        #Portas sala H
        self.__rooms.get('H').get('room').addDoor(Door(self.__rooms.get('G').get('room')))
        self.__rooms.get('H').get('room').addDoor(Door(self.__rooms.get('I').get('room')))
        self.__rooms.get('H').get('room').addDoor(Door(self.__rooms.get('K').get('room')))
        self.__rooms.get('H').get('room').addDoor(Door(self.__rooms.get('L').get('room')))
        #Portas sala I
        self.__rooms.get('I').get('room').addDoor(Door(self.__rooms.get('H').get('room')))
        self.__rooms.get('I').get('room').addDoor(Door(self.__rooms.get('J').get('room')))
        #Portas sala J
        self.__rooms.get('J').get('room').addDoor(Door(self.__rooms.get('F').get('room')))
        self.__rooms.get('J').get('room').addDoor(Door(self.__rooms.get('I').get('room')))
        self.__rooms.get('J').get('room').addDoor(Door(self.__rooms.get('M').get('room')))
        #Portas sala K
        self.__rooms.get('K').get('room').addDoor(Door(self.__rooms.get('G').get('room')))
        self.__rooms.get('K').get('room').addDoor(Door(self.__rooms.get('H').get('room')))
        self.__rooms.get('K').get('room').addDoor(Door(self.__rooms.get('N').get('room')))
        #Portas sala L
        self.__rooms.get('L').get('room').addDoor(Door(self.__rooms.get('H').get('room')))
        self.__rooms.get('L').get('room').addDoor(Door(self.__rooms.get('M').get('room')))
        #Portas sala M
        self.__rooms.get('M').get('room').addDoor(Door(self.__rooms.get('J').get('room')))
        self.__rooms.get('M').get('room').addDoor(Door(self.__rooms.get('L').get('room')))
        self.__rooms.get('M').get('room').addDoor(Door(self.__rooms.get('P').get('room')))
        #Portas sala N
        self.__rooms.get('N').get('room').addDoor(Door(self.__rooms.get('K').get('room')))
        self.__rooms.get('N').get('room').addDoor(Door(self.__rooms.get('O').get('room')))
        self.__rooms.get('N').get('room').addDoor(Door(self.__rooms.get('Q').get('room')))
        #Portas sala O
        self.__rooms.get('O').get('room').addDoor(Door(self.__rooms.get('N').get('room')))
        self.__rooms.get('O').get('room').addDoor(Door(self.__rooms.get('P').get('room')))
        #Portas sala P
        self.__rooms.get('P').get('room').addDoor(Door(self.__rooms.get('M').get('room')))
        self.__rooms.get('P').get('room').addDoor(Door(self.__rooms.get('O').get('room')))
        self.__rooms.get('P').get('room').addDoor(Door(self.__rooms.get('T').get('room')))
        #Portas sala Q
        self.__rooms.get('Q').get('room').addDoor(Door(self.__rooms.get('N').get('room')))
        self.__rooms.get('Q').get('room').addDoor(Door(self.__rooms.get('R').get('room')))
        #Portas sala R
        self.__rooms.get('R').get('room').addDoor(Door(self.__rooms.get('Q').get('room')))
        self.__rooms.get('R').get('room').addDoor(Door(self.__rooms.get('S').get('room')))
        #Portas sala S
        self.__rooms.get('S').get('room').addDoor(Door(self.__rooms.get('R').get('room')))
        self.__rooms.get('S').get('room').addDoor(Door(self.__rooms.get('T').get('room')))
        #Portas sala T
        self.__rooms.get('T').get('room').addDoor(Door(self.__rooms.get('P').get('room')))
        self.__rooms.get('T').get('room').addDoor(Door(self.__rooms.get('S').get('room')))
        self.__rooms.get('T').get('room').addDoor(Door(self.__rooms.get('U').get('room')))
        #Portas sala U
        self.__rooms.get('U').get('room').addDoor(Door(self.__rooms.get('T').get('room')))

    def createEnvironment(self):
        env = Environment()
        env.setRooms(self.__rooms)
        return env
