from queue import PriorityQueue

class AEstrela:
    def __init__(self, environment):
        self.__environment = environment
        self.__destiny = None
        self.__distance = {}
        self.__queue = PriorityQueue()
    
    #Custo Estimado
    def h(self, n):
        return self.__environment.distancia(n, self.__destiny)

    #Custo atual
    def g(self, n):
        return self.__distance.get(n).get('distance')

    def f(self, n):
        return self.h(n) + self.g(n)

    def getProximoNo(self, n):
        room = self.__environment.findRoom(n).get('room')
        choice = None
        for door in room.getDoors():
            label = door.getDestiny().getLabel()
            if(self.__distance.get(label) == None or self.__distance.get(label).get('open')):
                self.avalia(door.getDestiny(), room)
                f = self.f(label)
                if(choice == None):
                    choice = [label, f]
                else:
                    choice = [label, f] if f < choice[1] else choice
        return choice[0]

    def avalia(self, next, prev):
        if(prev != None):
            distance = self.__distance.get(prev.getLabel()).get('distance') + next.getArea()
        else:
            distance = next.getArea()
        self.__distance.update({next.getLabel():{'distance': distance, 'open': True}})

    def print(self):
        print("chegou")
        print("{}".format(self.__queue.qsize()))
    
    def search(self, root, destiny):
        self.__destiny = destiny
        self.avalia(self.__environment.findRoom(root).get('room'), None)
        self.__queue.put(root)

        while not self.__queue.empty():
            no = self.__queue.get()
            if(no == destiny):
                self.print()
                return

            next = self.getProximoNo(no)
            if(next != None):
                print("{}".format(no))
                self.__queue.put(next)
                self.__distance.get(next).update({'open': False})


        print("Não existe!")
        return 0