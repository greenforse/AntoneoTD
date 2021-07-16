import math
from abc import ABCMeta, abstractmethod
class Tower (metaclass=ABCMeta):
    def __init__(self,mouseCoord,sc):
        self.sc=sc
        self.x=mouseCoord[0]
        self.y=mouseCoord[1]
        self.target=None
        self.atackRadius = 200
        self.wirina=30
        self.dlina=30
        self.priceLvlUp = 30
    #@abstractmethod
    #def atack(self):
    #    pass

    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def lvlUp(self):
        pass


    def findEnemy (self,enemys):
       #rangeTarget = None
       if self.target==None:
           for enemy in enemys:
               kastil = ((self.x-enemy.x)**2)+((self.y-enemy.y)**2)
               if math.sqrt(kastil) <= self.atackRadius:
                  # print(math.sqrt(kastil))
                   self.target=enemy
                   #print("Выбрана цель")
                   break
       if self.target != None:
            kastil = ((self.x-self.target.x)**2)+((self.y-self.target.y)**2)
            if math.sqrt(kastil) >= self.atackRadius:
                self.target = None
            if self.target not in enemys:
                self.target = None
    #@abstractmethod
    #def lvlup(self):
    #    pass