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

    def findMenor(self):
        choice = None
        for label, dist in self.__distance.items():
            if(dist.get('open')):
                if(choice == None):
                    choice = [label, dist.get('distance')]
                else:
                    choice = [label, dist.get('distance')] if dist.get('distance') < choice[1] else choice
        
        return choice[0] if choice != None else None

    def getProximoNo(self):
        menor = self.findMenor()
        room = self.__environment.findRoom(menor).get('room')
        for door in room.getDoors():
            label = door.getDestiny().getLabel()
            if(self.__distance.get(label) == None or self.__distance.get(label).get('open')):
                self.avalia(door.getDestiny(), room)
        return menor

    def avalia(self, next, prev):
        l = None
        if(prev != None):
            l = prev.getLabel()
            distance = self.__distance.get(l).get('distance') + next.getArea()
        else:
            distance = next.getArea()
        
        if(self.__distance.get(next.getLabel()) == None):
            self.__distance.update({next.getLabel():{'distance': distance, 'prev': l ,'open': True}})


    def print(self, node):
        arr = [node]
        while node != None:
            arr.insert(0, node)
            node = self.__distance.get(node).get('prev')
        print(arr)
    
    def search(self, root, destiny):
        if(self.__environment.findRoom(root) == None or self.__environment.findRoom(destiny) == None):
            print("Não existe!")
            return

        self.__destiny = destiny
        self.avalia(self.__environment.findRoom(root).get('room'), None)
        self.__queue.put(root)

        no = root
        while not self.__queue.empty():
            if(no == destiny):
                self.print(no)
                return
            
            next = self.getProximoNo()
            if(next != None):
                no = next
                self.__queue.put(next)
                self.__distance.get(next).update({'open': False})
            else:
                self.__queue.get()

        print("Não existe!")
        return