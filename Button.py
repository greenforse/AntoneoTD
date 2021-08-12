import pygame as pg

class Button():
    def __init__(self,wirina,dlina,x,y,color,function,sc,txt,player,sizeTxt):
        self.wirina = wirina
        self.dlina = dlina
        self.color = color
        self.function = function
        self.sc = sc
        self.txt = txt
        self.x = x
        self.y = y
        self.player=player
        self.sizeTxt = sizeTxt
        #self.fontObj = pg.font.Font('18963.ttf', 24)
    def viewButton(self):
        self.fontObj = pg.font.Font('18963.ttf', self.sizeTxt)
        text = str(self.txt)
        pg.draw.rect(self.sc,self.color,(self.x,self.y, self.wirina,self.dlina))
        textSurfaceObj = self.fontObj.render((f"{text}") , False, (0,0,0), self.color)
        self.sc.blit(textSurfaceObj,(self.x,self.y+self.dlina//4))

        #pg.draw.rect(self.sc,(255,255,255),(self.x,self.y, self.wirina,self.dlina))
        # mecto dlya txt

    def operation(self,x,y):
        self.function(self.player,(x,y),self.sc)
