
class Player():
    def __init__(self):
        #self.sc=sc
        self.gold = 50 
        self.livePoints = 20

    def buyTower(self,price):
        if self.gold >= price:
            self.gold -= price
            return True
        else: return False
    
    def lossLivePoints(self):
        if self.livePoints > 0:
            self.livePoints -= 1
            return True
        else: False
