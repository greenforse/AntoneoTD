from State import State
from FinishMenuState import FinishMenuState
class GameState(State):
    def __init__(self,game):
        self.game=game
    
    def init(self):
        self.game.gameInit()

    def processEvents(self):
        self.game.inputMouseButtonInGame()
        if not self.game.Anton.play:
            self.game.closeAllGameMenu()
            self.game.changeState(FinishMenuState)

    def draw(self,time):
        self.game.drawGame(time)