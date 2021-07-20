from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
  def __init__(self, menu):
    self.menu = menu

  @abstractmethod
  def init(self,mouseCoord):
    pass

  @abstractmethod
  def processEvents(self, mouseCoord):
    pass

  @abstractmethod
  def draw (self,time):
    pass