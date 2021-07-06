from Enemy import Enemy
import pygame as pg
class Bullet():
    def __init__(self,LimitSpeedBullet,x,y,sc,damage,target):
        self.bulletX=x
        self.bulletY=y
        self.LimitSpeedBullet = LimitSpeedBullet
        self.sc=sc
        self.damage = damage
        self.oneTime = 0
        self.deltaTime = 5
        self.strike = False
        self.enemy = target
    def atack (self,secondTime):
        if self.deltaTime <= secondTime - self.oneTime:
            if self.bulletX > self.enemy.x:
                if self.bulletX - self.enemy.x < self.LimitSpeedBullet:
                    self.bulletX = self.enemy.x
                else: self.bulletX -= self.LimitSpeedBullet
            else:
                if self.enemy.x - self.bulletX < self.LimitSpeedBullet:
                    self.bulletX = self.enemy.x
                else: self.bulletX += self.LimitSpeedBullet

            if self.bulletY > self.enemy.y:
                if self.bulletY - self.enemy.y < self.LimitSpeedBullet:
                    self.bullety = self.enemy.y
                else: self.bulletY -= self.LimitSpeedBullet
            else:
                if self.enemy.y - self.bulletY< self.LimitSpeedBullet:
                    self.bulletY = self.enemy.y
                else: self.bulletY += self.LimitSpeedBullet
            if self.bulletY==self.enemy.y and self.bulletX == self.enemy.x and not self.strike:
                self.enemy.HP-= self.damage
                self.strike = True
            self.oneTime = secondTime
    def bulletWiew(self):
        if not self.strike:
            pg.draw.rect(self.sc,(100,0,30),(self.bulletX,self.bulletY,10,10))
    #def atack1  (self,enemy):
    #
    #    #speedBullet = (self.bulletX-enemy.x) // (self.bulletY-enemy.y)
    #    if self.bulletX - enemy.x > self.bulletY-enemy.y:
    #        self.bulletX += self.LimitSpeedBullet
    #    else:
    #        self.bulletY + 



        #if speedBullet == 0:
        #    speedBullet = (self.bulletY-enemy.y) // (self.bulletX-enemy.x)
        #    if self.LimitSpeedBullet > speedBullet +1:
        #        if self.bulletY-enemy.y > 0:
        #            self.bulletY -= self.LimitSpeedBullet
        #            if self.bulletX - enemy.x > 0:
        #                self.bulletX -= self.LimitSpeedBullet // speedBullet
        #            else:self.bulletX += self.LimitSpeedBullet // speedBullet
        #        else: self.bulletY += self.LimitSpeedBullet
        #    else: self.bulletY += self.LimitSpeedBullet
        #else:
        #    if self.LimitSpeedBullet < speedBullet + 1 :
        #        self.bulletX += self.LimitSpeedBullet
        #        self.bulletY += self.LimitSpeedBullet // speedBullet
        #    else: self.bulletX += self.LimitSpeedBullet 