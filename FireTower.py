from Tower import Tower
import math
import cmath
from Bullet import Bullet
import pygame as pg
class FireTower(Tower):
    def __init__ (self,atackSpeed,damage,mouseCoord,sc):
        self.atackSpeed=atackSpeed
        self.damage=damage
        self.x=mouseCoord[0]
        self.y=mouseCoord[1]
        self.exp=0
        self.LimitSpeedBullet=2
        self.bulletX=self.x
        self.bulletY=self.y
        self.atackRadius=50
        self.timeCooldown = 10
        self.target=None
        self.oneTime=0
        self.bullet = Bullet(self.LimitSpeedBullet,self.x,self.y,sc)
        self.sc = sc
    def observ(self,enemys):
        if self.target==None:
            for enemy in enemys:
                kastil = (self.x-enemy.x)+(self.y-enemy.y)
                if kastil < 0:
                    kastil *= -1
                if math.sqrt(kastil) <= self.atackRadius:
                    self.target=enemy
                    break

                    
    def atack(self,secondTime):
        if secondTime-self.oneTime >= self.timeCooldown and self.target != None:
            #self.bullet.atack(self.target)
            self.bullet.atack1(self.target)
            self.oneTime=secondTime
            
    def live (self,enemys,secondTime):
        self.observ(enemys)
        self.atack(secondTime)
        pg.draw.rect(self.sc,(255,255,255),(self.x,self.y, 30,30))
        #self.bullet.live()
        pg.draw.rect(self.sc,(100,0,30),(self.bullet.bulletX,self.bullet.bulletY,10,10))