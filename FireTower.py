from Tower import Tower
import math
import cmath
from Bullet import Bullet
import pygame as pg
class FireTower(Tower):
    def __init__ (self,mouseCoord,sc):
        self.price = 20
        self.atackSpeed=10
        self.damage=100
        self.x=mouseCoord[0]
        self.y=mouseCoord[1]
        self.exp=0
        self.LimitSpeedBullet=4
        self.bulletX=self.x
        self.bulletY=self.y
        self.atackRadius=200
        self.timeCooldown = 1500
        self.target=None
        self.oneTime=0
        #self.bullet = Bullet(self.LimitSpeedBullet,self.x,self.y,sc,damage,self.target)
        self.sc = sc
        self.bullets=[]
        self.wirina=30
        self.dlina=30
        self.lvl=0
    def findEnemy (self,enemys):
        #rangeTarget = None
        if self.target==None:
            for enemy in enemys:
                kastil = ((self.x-enemy.x)**2)+((self.y-enemy.y)**2)
                if math.sqrt(kastil) <= self.atackRadius:
                   # print(math.sqrt(kastil))
                    self.target=enemy
                    #print("Выбрана цель")
                    break
        if self.target != None:
            kastil = ((self.x-self.target.x)**2)+((self.y-self.target.y)**2)
            if math.sqrt(kastil) >= self.atackRadius:
                    self.target = None
                    
    def atack(self,secondTime):
        if self.target != None:
            if secondTime-self.oneTime >= self.timeCooldown and self.target != None:
                bullet = Bullet(self.LimitSpeedBullet,self.x,self.y,self.sc,self.damage, self.target)
                self.bullets.append (bullet)
                self.oneTime=secondTime
            if self.target == None:
                for i in range(len(self.bullets)):
                    if self.bullets[i].strike: #bulletX == self.target.x and self.bullets[i].bulletY == self.target.y:
                        del self.bullets[i]
            for bullet in self.bullets:
                bullet.atack(secondTime)
                bullet.bulletWiew()
            if self.target.HP <= 0:
                self.target = None
    
    def lvlUp(self):
        self.damage+=100
        self.timeCooldown -=100
        
    def live (self,enemys,secondTime):
        self.findEnemy(enemys)
        self.atack(secondTime)
        pg.draw.rect(self.sc,(255,255,255),(self.x,self.y, self.wirina,self.dlina))
        self.viewLvlup()
        #self.bullet.live()
    
    def viewLvlup(self):
        if self.lvl >= 1:
            pg.draw.rect(self.sc,(255,0,0),(self.x+self.wirina,(self.y+self.dlina)-(5*self.lvl), 5,5))