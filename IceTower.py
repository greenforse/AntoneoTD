
import math
from Tower import Tower
from Enemy import Enemy
import pygame as pg

class IceTower(Tower):
    def __init__(self,coord,sc):
        self.price=20
        self.x=coord[0]
        self.y=coord[1]
        self.deltatime = None
        self.target=None
        self.atackRadius = 150
        self.sc=sc
        self.targetAura=[]
        self.timeCooldown = 1500
        self.oneTime = 0
        self.wirina=30
        self.dlina=30
    #def findEnemy(self, enemys):
    #    return super().findEnemy(enemys)
#
    def atack(self,enemys):
        if self.target != None:
                pg.draw.circle(self.sc,(0,0,255),(self.target.x,self.target.y),self.atackRadius,8)
                for enemy in enemys:
                    if math.sqrt(((self.target.x-enemy.x)**2)+((self.target.y-enemy.y)**2)) < self.atackRadius:
                        enemy.frozen = True
                    else: enemy.frozen = False
                if self.target.HP <= 0:
                    self.target = None
    
    def lvlUp(self):
        self.atackRadius+=50

    def live(self,enemys,secondTime):
        self.findEnemy(enemys)
        self.atack(enemys)
        pg.draw.rect(self.sc,(0,0,255),(self.x,self.y, self.wirina,self.dlina))



