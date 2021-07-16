from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
  def __init__(self, menu):
    self.menu = menu

  @abstractmethod
  def startMenu(self,mouseCoord):
    pass

  @abstractmethod
  def gameMenu(self, mouseCoord):
    pass

  @abstractmethod
  def finishMenu (self,mouseCoord):
    pass