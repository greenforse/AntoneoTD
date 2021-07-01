
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

    #@abstractmethod
    #def lvlup(self):
    #    pass