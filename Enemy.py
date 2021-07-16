import pygame as pg
RED=(255,0,0)
WHITE = (255, 255, 255)

class Enemy():
    def __init__(self,road,sc,hp):
        self.startSpeed = 5
        self.x = road.road[0][0]
        self.y = road.road[0][1]
        self.radius= 20
        self.HP=hp
        self.step=1
        self.lastStep = 0
        self.lastStep2 = 0
        self.sc=sc
        self.atackers = []
        self.napravlenie = 0
        self.frameNumber = 0 # номер кадра анимации 
        self.dlina=60
        self.wirina=25
        self.right1 = pg.image.load("TankWL.png")
        self.right1.set_colorkey(WHITE)
        self.right1=pg.transform.scale(self.right1,(self.dlina,self.wirina))
        self.right2 = pg.image.load("TankWN.png")
        self.right2.set_colorkey(WHITE)
        self.right2=pg.transform.scale(self.right2,(self.wirina,self.dlina))
        self.right3 = pg.image.load("TankWW.png")
        self.right3.set_colorkey(WHITE)
        self.right3=pg.transform.scale(self.right3,(self.wirina,self.dlina))
        #right4 = pg.image.load("направо4.png")
        #right4=pg.transform.scale(right4,(dlina,wirina))
        self.animation=[self.right1,self.right2,self.right3] # массив направлений с кадрами анимаций 
        self.swichNapravlenie = 0
        self.frozen=False
    def go (self,road,deltaTime):
        if self.frozen:
            self.speed = self.startSpeed // 2
        else: self.speed = self.startSpeed

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
            #if self.x > road[self.step][0]:
            #    if self.x - road[self.step][0] <= self.speed : #убрал т.к. в таком направлении пока враги не двигаются 
            #        self.x=road[self.step][0]
            #        self.step+=1
            #        #print("Достигнуто по -х",self.step)
            #    else:
            #        self.x-=self.speed
            #        self.napravlenie=1
            if self.y < road[self.step][1]:
                if road[self.step][1]-self.y <= self.speed:
                    self.y=road[self.step][1]
                    self.step+=1
                    #print("Достигнуто по y",self.step)
                else:
                    self.y+=self.speed
                    self.napravlenie = 1
            if self.y > road[self.step][1]:
                if self.y - road[self.step][1] <= self.speed :
                    self.y=road[self.step][1]
                    self.step+=1
                    #print("Достигнуто по y",self.step)
                else:
                    self.y-=self.speed
                    self.napravlenie = 2
            self.lastStep = deltaTime

    def viewEnemy(self,deltaTime):
        if deltaTime - self.lastStep2 >=1000:
            if self.napravlenie == 0:
                self.sc.blit(self.animation[self.napravlenie],(self.x-self.dlina//2,self.y-self.wirina//2))
            else:self.sc.blit(self.animation[self.napravlenie],(self.x-self.wirina//2,self.y-self.dlina//2))
    def viewEnemyAnimation(self,deltaTime):
        if self.swichNapravlenie != self.napravlenie: #сравниваем направление 
            self.frameNumber = 0

        if self.napravlenie==8:
            self.sc.blit(self.animation[self.napravlenie][self.frameNumber],(self.x-self.dlina,self.y-self.wirina//2)) # тут я должен что то нарисовать 
        else:
            pg.draw.circle(self.sc,RED,(self.x,self.y),self.radius)

        if deltaTime - self.lastStep2 >=1000:
            self.frameNumber+=1
        if self.frameNumber == len(self.animation[self.napravlenie]):
            self.frameNumber = 0
        rstep=False
        #if self.x >= (road[self.step][0]-(self.speed)) and self.x <= (road[self.step][0]+(self.speed)) and self.y >= (road[self.step][1]-(self.speed)) and self.y <= (road[self.step][1]+(self.speed)) :
        if (self.road[self.step][0] - self.road[self.step-1][0]) / (self.x - self.road[self.step-1][0]) != (self.road[self.step][0]-self.road[self.step-1][1] ) / (self.road[self.step][1] - self.y) :
            self.x = self.road[self.step][0]
            self.y = self.road[self.step][1]
            self.step+=1
            print("достигнут шаг",self.step)

        if self.x  <  self.road[self.step][0]:
            self.x +=self.speed
            print("+x")
            rstep=True
        elif self.x  >  self.road[self.step][0]  :
            if rstep:
                self.x -= (self.speed//2)
                print("Половина-х")
            else: 
                self.x -= self.speed
                print("-x")
            rstep=True
        if self.y < self.road[self.step][1] :
            if rstep:
                self.y += (self.speed//2)
            else:
                self.y += self.speed
            rstep=True
        elif self.y > self.road[self.step][1] :
            if rstep:
                self.y -= (self.speed//2)
            else: 
                self.y -= self.speed
            
        