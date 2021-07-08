from Button import Button
import pygame as pg
from Button import Button
class Menu():
    def __init__(self,wirina,dlina,color,sc,player):
        self.wirina = wirina
        self.dlina = dlina
        self.color = color
        self.buttons = []
        self.deltabuttonY = self.dlina
        self.sc = sc
        self.x = 0
        self.y = 0
        self.inter = False
        self.player = player

    def addCoordinate(self,coord): 
        if not self.inter: # первое нажатие кнопки вывода меню 
            self.x=coord[0] # забиваем координаты
            self.y=coord[1]
            self.inter = True # Флажок открытия меню
            self.restructButtons()
        else:
            self.inter = False # второе нажатие, убираем флажок, закрывается меню


    def selectButton(self,coord):
        if self.inter:
            if coord[0] >= self.x and coord[0] <= self.x + self.wirina: #Проверяем попадаем ли мы в поле меню по х
                if coord[1] >=self.y and coord[1] <= self.y + self.dlina:# по y
                    print("Попали по меню")
                    for button in self.buttons:                       # проходимся по всем кнопкам, определяем на какую нажали
                        if coord[0] >= button.x and coord[0] <= button.x + button.wirina:
                            if coord[1] >= button.y and coord[1] <= button.y+button.dlina :
                                print("Попали по кнопочке")
                                button.operation(self.x,self.y)
                                self.inter = False

    def viewMenu(self):
        if self.inter: # если меню открыто то показываем его 
            pg.draw.rect(self.sc,(0,0,255),(self.x,self.y, self.wirina,self.dlina))
            for button in self.buttons:
                button.viewButton()

    def addButton(self,txt,color,function):
        button=Button(self.wirina,self.deltabuttonY,self.x,self.y+self.deltabuttonY,color,function, self.sc,txt,self.player)
        self.buttons.append(button)
        self.deltabuttonY = self.dlina//len(self.buttons)
        for button in self.buttons:
            button.dlina = self.deltabuttonY

    def delButtons(self):
        self.buttons=[]

    def restructButtons(self):  #Расстановка кнопок в зависимости от положения Меню
        for i in range (len(self.buttons)):
            self.buttons[i].y = self.y + (self.deltabuttonY * (i))
            self.buttons[i].x = self . x
            
            