
class Player():
    def __init__(self):
        #self.sc=sc
        self.gold = 50 
        self.livePoints = 20
        self.allTowers=[]
        self.play=False

    def buyTower(self,price):
        if self.gold >= price:
            self.gold -= price
            return True
        else: return False
    
    def lvlUp(self,tower):
        if tower.price <= self.gold:
            self.gold -= tower.price
            tower.lvlUp()

    def lossLivePoints(self): #Трата очков при прохождении врагов конечной точки и возвращение 
        if self.livePoints > 0:# False очки если закончились(проигрыш)
            self.livePoints -= 1
            return True
        else: False

    def hitTower(self,coord):
        hit=False
        for tower in self.allTowers:
            if coord[0] <= tower.x + tower.wirina //2 and coord[0] >= tower.x-tower.wirina//2:
                if coord[1] <= tower.y + tower.dlina//2 and coord[1] >= tower.y-tower.dlina//2:
                    hit = True
        return hit

    def readyPlay(self):
        self.play=True

    def notReadyPlay(self):
        self.play=False    