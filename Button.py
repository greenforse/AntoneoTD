import pygame as pg

class Button():
    def __init__(self,wirina,dlina,x,y,color,function,sc,txt,player):
        self.wirina = wirina
        self.dlina = dlina
        self.color = color
        self.function = function
        self.sc = sc
        self.txt = txt
        self.x = x
        self.y = y
        self.player=player
    def viewButton(self):
        fontObj = pg.font.Font('18963.ttf', 24)
        text = str(self.txt)
        pg.draw.rect(self.sc,self.color,(self.x,self.y, self.wirina,self.dlina))
        textSurfaceObj = fontObj.render((f"{text}") , False, (0,0,0), self.color)
        self.sc.blit(textSurfaceObj,(self.x,self.y))

        #pg.draw.rect(self.sc,(255,255,255),(self.x,self.y, self.wirina,self.dlina))
        # mecto dlya txt

    def operation(self,x,y):
        self.function(self.player,(x,y),self.sc)
