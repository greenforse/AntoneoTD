import pygame as pg
class RoadEnemy():
    def __init__(self):
        self.road=[(5, 385),(115, 385),(115, 175),(250, 175),(250, 445),(450, 445),(450, 300),(500, 300),(680,300)]
    
    def addRect(self,rect):
        self.roadList.append(rect)
    
    #def roadline(self):
    #    for rect in self.roadList:
    #        #centr = rect