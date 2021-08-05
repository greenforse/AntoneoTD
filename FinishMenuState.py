from State import State
import GameState as gs
class FinishMenuState(State):

    def __init__(self,game):
        self.game=game
    
    def init(self):
        self.game.buildFinishMenu()
        self.game.initAndStopFinishMenu()

    def processEvents(self):
        self.game.inputMouseButtonInBigMenu()
        if self.game.Anton.play:
            self.game.initAndStopFinishMenu()
            self.game.changeState(gs.GameState)

    
    def draw(self,time):
        self.game.drawFinishMenu(time)
