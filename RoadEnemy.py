import pygame as pg
class RoadEnemy():
    def __init__(self):
        self.road=[(5, 385),(115, 385),(115, 175),(250, 175),(250, 445),(450, 445),(450, 300),(500, 300),(680,300)]
        self.wirina=60

    def blockSpawnUnit(self,pointTower):
        permission = True
        for i in range(len(self.road)-1):
            if self.road[i+1][0] - self.road[i][0] > self.road[i+1][1]-self.road[i][1]: #Запрет спавна на участах дорог +х
               if pointTower[0] >= self.road[i][0] - self.wirina//2 and pointTower[0] <= self.road[i+1][0] + self.wirina//2:
                   if pointTower[1] >= self.road[i][1]-self.wirina and pointTower[1] <= self.road[i+1][1]+(self.wirina//2):
                       permission = False
                       #print("Запрет спавна")
            if self.road[i+1][0]-self.road[i][0] < self.road[i+1][1]-self.road[i][1]:    #Запрет спавна на участке +Y
                #print("Mi syda zawli")
                if  pointTower[1] >= self.road[i][1]- self.wirina//2 and pointTower[1] <= self.road[i+1][1]+self.wirina//2:
                    if pointTower[0] >= self.road[i][0]-(self.wirina//2) and pointTower[0] <= self.road[i+1][0]+self.wirina//2:
                        permission = False
                        #print ("Запрещено")
            if self.road[i+1][0]-self.road[i][0] < self.road[i][1]-self.road[i+1][1]: #Запрет спавна на участке -Y
                #print("123")
                if pointTower[1] <= self.road[i][1] + self.wirina//2 and pointTower[1] >= self.road[i+1][1] - self.wirina//2:
                    #print("Мы тута зашли")
                    if pointTower[0] >= self.road[i][0]-(self.wirina) and pointTower[0] <= self.road[i+1][0]+self.wirina:
                        permission = False
                        #print ("Запрещено -Y")
        return permission

#

            

    #def addRect(self,rect):
    #    self.roadList.append(rect)
    
    #def roadline(self):
    #    for rect in self.roadList:
    #        #centr = rect