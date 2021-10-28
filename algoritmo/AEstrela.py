from queue import PriorityQueue
import queue
from environment.Environment import Environment

class AEstrela:
    def __init__(self, environment):
        self.__environment = environment
        self.__destiny = None
        self.__queue = PriorityQueue()
    
    #Custo Estimado
    def h(self, n):
        return 0

    #Custo atual
    def g(self, n):
        return 0

    def f(self, n):
        return 
    
    def search(self,root, destiny):
        self.__destiny = destiny
        # TODO vai dar erro, o root é uma label
        self.__queue.put((self.h(root), root, [root]))
        
        while not self.__queue.empty():
            
            pass

        return 0