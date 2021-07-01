from Enemy import Enemy
import pygame as pg
class Bullet():
    def __init__(self,LimitSpeedBullet,x,y,sc):
        self.bulletX=x
        self.bulletY=y
        self.LimitSpeedBullet = LimitSpeedBullet
        self.sc=sc
    def atack (self,enemy):
        if self.bulletX > enemy.x:
            if self.bulletX - enemy.x < self.LimitSpeedBullet:
                self.bulletX = enemy.x
            else: self.bulletX -= self.LimitSpeedBullet
        else:
            if enemy.x - self.bulletX < self.LimitSpeedBullet:
                self.bulletX = enemy.x
            else: self.bulletX += self.LimitSpeedBullet

        if self.bulletY > enemy.y:
            if self.bulletY - enemy.y < self.LimitSpeedBullet:
                self.bullety = enemy.y
            else: self.bulletY -= self.LimitSpeedBullet
        else:
            if enemy.y - self.bulletY< self.LimitSpeedBullet:
                self.bulletY = enemy.y
        
            else: self.bulletY += self.LimitSpeedBullet

    def atack1  (self,enemy):
        speedBullet = (self.bulletX-enemy.x) // (self.bulletY-enemy.y)
        if speedBullet == 0:
            speedBullet = (self.bulletY-enemy.y) // (self.bulletX-enemy.x)
            if self.LimitSpeedBullet > speedBullet +1:
                if self.bulletY-enemy.y > 0:
                    self.bulletY -= self.LimitSpeedBullet
                    if self.bulletX - enemy.x > 0:
                        self.bulletX -= self.LimitSpeedBullet // speedBullet
                    else:self.bulletX += self.LimitSpeedBullet // speedBullet
                else: self.bulletY += self.LimitSpeedBullet
            else: self.bulletY += self.LimitSpeedBullet
        else:
            if self.LimitSpeedBullet < speedBullet + 1 :
                self.bulletX += self.LimitSpeedBullet
                self.bulletY += self.LimitSpeedBullet // speedBullet
            else: self.bulletX += self.LimitSpeedBullet 