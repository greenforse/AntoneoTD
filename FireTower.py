from Tower import Tower


class FireTower(Tower):
    def __init__ (self,atackSpeed,damage,x,y):
        self.atackSpeed=atackSpeed
        self.damage=damage
        self.x=x
        self.y=y
        self.exp=0
        self.LimitSpeedBullet=30
        self.bulletX=self.x
        self.bulletY=self.y
        self.atackRadius=100

    def observ(self):
        pass

    def atack(self,enemy):
        speedBullet = (self.bulletX-enemy.x) // (self.bulletY-enemy.y)
        if speedBullet == 0:
            speedBullet = (self.bulletY-enemy.y) // (self.bulletX-enemy.x)
            if self.LimitSpeedBullet > speedBullet +1:
                self.bulletY += self.LimitSpeedBullet
                self.bulletX += self.LimitSpeedBullet // speedBullet
            else: self.bulletY += self.LimitSpeedBullet
        else:
            if self.LimitSpeedBullet > speedBullet + 1 :
                self.bulletX += self.LimitSpeedBullet
                self.bulletY += self.LimitSpeedBullet // speedBullet
            else: self.bulletX += self.LimitSpeedBullet

    def getCooerdinat (self):
        return(self.x,self.y)
        