import math
from abc import ABCMeta, abstractmethod
class Tower (metaclass=ABCMeta):
    def __init__(self,atackSpeed,damage,x,y):
        self.atackSpeed=atackSpeed
        self.damage=damage
        self.x=x
        self.y=y
        self.exp=0

    @abstractmethod
    def atack(self):
        pass
    
    @abstractmethod
    def live(self):
        pass

    def findEnemy (self,enemys):
        if self.target==None:
            for enemy in enemys:
                kastil = (self.x-enemy.x)+(self.y-enemy.y)
                if kastil < 0:
                    kastil *= -1
                if math.sqrt(kastil) <= self.atackRadius:
                    self.target=enemy
                    break
    
    #@abstractmethod
    #def lvlup(self):
    #    pass