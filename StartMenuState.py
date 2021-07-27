from GameState import GameState
from State import State

class StartMenuState(State):
    def __init__(self,game):
        self.game=game
    
    def init(self):
        self.game.buildStartMenu()
        self.game.initStopStartMenu()

    def processEvents(self):
        self.game.inputMouseButtonStartMenu()
        if self.game.Anton.play:
            self.game.initStopStartMenu()
            self.game.changeState(GameState)
            
    def draw(self):
        self.game.drawStartMenu()


