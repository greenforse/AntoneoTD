import pygame as pg
from Tower import Tower
class LazerTower(Tower):
    def __init__(self,mouseCoord,sc):
        self.x=mouseCoord[0]
        self.y=mouseCoord[1]
        self.price=20
        self.oneTime=0
        self.timeCooldown = 100
        self.damage=10
        self.sc=sc
        self.wirina=40
        self.dlina=40
        self.target=None
        self.atackRadius=200
        self.picture = pg.image.load("LazerTow.png")
        self.picture.set_colorkey((255,255,255))
        self.picture=pg.transform.scale(self.picture,(self.dlina,self.wirina))
        self.lvl=0
        #self.lazer=False
        #self.lazerTime=0
    def atack(self,secondTime):
        if self.target != None:
            pg.draw.line(self.sc,(50,100,255),(self.x,self.y),(self.target.x,self.target.y),3)
            if self.timeCooldown <= secondTime-self.oneTime:
                self.target.HP -= self.damage
                #self.lazer=True
                self.oneTime = secondTime
            #if self.lazer and self.timeCooldown*3 <= secondTime-self.lazerTime :
            #    pg.draw.line(self.sc,(50,100,255),(self.x,self.y),(self.target.x,self.target.y),3)
            #    self.lazerTime=secondTime
                
            if self.target.HP <= 0:
                self.target = None
    
    def lvlUp(self):
        self.damage+=5
        self.lvl+=1

    def live(self,enemys,secondTime):
        self.findEnemy(enemys)
        self.sc.blit(self.picture,(self.x-self.dlina//2,self.y-self.wirina//2))
        self.viewLvlup()
        #pg.draw.rect(self.sc,(0,255,0),(self.x-self.wirina//2,self.y-self.dlina//2, self.wirina,self.dlina))
        self.atack(secondTime) 
    
    def viewLvlup(self):
        if self.lvl >= 1:
            pg.draw.rect(self.sc,(255,0,0),(self.x+self.wirina//2,(self.y+self.dlina//2)-(5*self.lvl), 5,5))
