class Environment:
    def __init__(self):
        self.__rooms = {}

    def getRooms(self):
        return self.__rooms
    
    def setRooms(self, rooms):
        self.__rooms = rooms
    
    def addRoom(self, room, coordinates):
        dict = {
            'room': room,
            'coordinates': coordinates
        }
        self.__rooms.update({room.getLabel(): dict})

    def findRoom(self, label):
        return self.__rooms[label]
    
    def visit(self):
        print("Salas: ", len(self.__rooms.values()) ,"\n")
        for room in self.__rooms.values():
            print("Sala ", room.get('room').getLabel() ,"!\n")
            for door in room.get('room').getDoors():
                print("\t Porta para ", door.getDestiny().getLabel(),".")

    def distancia(self, labelRoot, labelIntention):
        locationRoot = self.__rooms.get(labelRoot).get('coordinates')
        locationIntention = self.__rooms.get(labelIntention).get('coordinates')
        distance = distanciaManhattan(locationRoot.get('x'), locationIntention.get('x'), locationRoot.get('y'), locationIntention.get('y'))
        return distance

def distanciaManhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)