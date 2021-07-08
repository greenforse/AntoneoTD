import pygame as pg
RED=(255,0,0)
WHITE = (255, 255, 255)
dlina=40
wirina=40
right1 = pg.image.load("направо1.png")
right1.set_colorkey(WHITE)
right1=pg.transform.scale(right1,(dlina,wirina))
right2 = pg.image.load("направо2.png")
right2.set_colorkey(WHITE)
right2=pg.transform.scale(right2,(dlina,wirina))
right3 = pg.image.load("направо3.png")
right3.set_colorkey(WHITE)
right3=pg.transform.scale(right3,(dlina,wirina))
right4 = pg.image.load("направо4.png")
right4.set_colorkey(WHITE)
right4=pg.transform.scale(right4,(dlina,wirina))
class Enemy():
    def __init__(self,road,sc):
        self.speed = 5
        self.x = road.road[0][0]
        self.y = road.road[0][1]
        self.radius= 20
        self.HP=500
        self.step=1
        self.lastStep = 0
        self.lastStep2 = 0
        self.sc=sc
        self.atackers = []
        self.napravlenie = 0
        self.frameNumber = 0 # номер кадра анимации 
        self.animation=[[right1,right2,right3,right4],[],[],[]] # массив направлений с кадрами анимаций 
        self.swichNapravlenie = 0
    def go (self,road,deltaTime):
        if deltaTime - self.lastStep >= 100:
            self.swichNapravlenie = self.napravlenie #запоминаем направление чтоб потом в Функции показа сравнить 
            if self.x < road[self.step][0]:
                if road[self.step][0]-self.x <= self.speed:
                    self.x=road[self.step][0]
                    self.step+=1
                    #print("Достигнуто по +х",self.step)
                else:
                    self.x+=self.speed
                    self.napravlenie=0
            if self.x > road[self.step][0]:
                if self.x - road[self.step][0] <= self.speed :
                    self.x=road[self.step][0]
                    self.step+=1
                    #print("Достигнуто по -х",self.step)
                else:
                    self.x-=self.speed
                    self.napravlenie=1
            if self.y < road[self.step][1]:
                if road[self.step][1]-self.y <= self.speed:
                    self.y=road[self.step][1]
                    self.step+=1
                    #print("Достигнуто по y",self.step)
                else:
                    self.y+=self.speed
                    self.napravlenie = 2
            if self.y > road[self.step][1]:
                if self.y - road[self.step][1] <= self.speed :
                    self.y=road[self.step][1]
                    self.step+=1
                    #print("Достигнуто по y",self.step)
                else:
                    self.y-=self.speed
                    self.napravlenie = 3
            self.lastStep = deltaTime

    def viewEnemy(self,deltaTime):
        if self.swichNapravlenie != self.napravlenie: #сравниваем направление 
            self.frameNumber = 0

        if self.napravlenie==8:
            self.sc.blit(self.animation[self.napravlenie][self.frameNumber],(self.x,self.y-wirina//2)) # тут я должен что то нарисовать 
        else:
            pg.draw.circle(self.sc,RED,(self.x,self.y),self.radius)

        if deltaTime - self.lastStep2 >=1000:
            self.frameNumber+=1
        if self.frameNumber == len(self.animation[self.napravlenie]):
            self.frameNumber = 0

        #rstep=False
        ##if self.x >= (road[self.step][0]-(self.speed)) and self.x <= (road[self.step][0]+(self.speed)) and self.y >= (road[self.step][1]-(self.speed)) and self.y <= (road[self.step][1]+(self.speed)) :
        #if (road[self.step][0] - road[self.step-1][0]) / (self.x - road[self.step-1][0]) != (road[self.step][0]-road[self.step-1][1] ) / (road[self.step][1] - self.y) :
        #    self.x = road[self.step][0]
        #    self.y = road[self.step][1]
        #    self.step+=1
        #    print("достигнут шаг",self.step)
#
        #if self.x  <  road[self.step][0]:
        #    self.x +=self.speed
        #    print("+x")
        #    rstep=True
        #elif self.x  >  road[self.step][0]  :
        #    if rstep:
        #        self.x -= (self.speed//2)
        #        print("Половина-х")
        #    else: 
        #        self.x -= self.speed
        #        print("-x")
        #    rstep=True
        #if self.y < road[self.step][1] :
        #    if rstep:
        #        self.y += (self.speed//2)
        #    else:
        #        self.y += self.speed
        #    rstep=True
        #elif self.y > road[self.step][1] :
        #    if rstep:
        #        self.y -= (self.speed//2)
        #    else: 
        #        self.y -= self.speed
            
        