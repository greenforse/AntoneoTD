from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
  #def __init__(self, menu):
  @abstractmethod
  def init(self):
    pass

  @abstractmethod
  def processEvents(self):
    pass

  @abstractmethod
  def draw (self):
    pass