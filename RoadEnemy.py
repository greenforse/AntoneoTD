import pygame as pg
pg.init()

class RoadEnemy():
    def __init__(self):
        self.roadList=[]

    def addRect(self,rect):
        self.roadList.append(rect)
    
    #def roadline(self):
    #    for rect in self.roadList:
    #        #centr = rect
#