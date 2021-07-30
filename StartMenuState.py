from GameState import GameState
from State import State

class StartMenuState(State):
    def __init__(self,game):
        self.game=game
    
    def init(self):
        self.game.buildStartMenu()
        self.game.initAndStopStartMenu()

    def processEvents(self):
        self.game.inputMouseButtonInBigMenu()
        if self.game.Anton.play:
            self.game.initAndStopStartMenu()
            self.game.changeState(GameState)
            
    def draw(self,time):
        self.game.drawStartMenu(time)


