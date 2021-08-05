
from Menu import Menu
from RoadEnemy import RoadEnemy
import pygame as pg
from Player import Player
import GameSetup as GS
import ButtonFunction as BF
from Enemy import Enemy
from StartMenuState import StartMenuState
class Game():

    def __init__(self):
        
        self.windowSize=(700,700)
        self.screen = pg.display.set_mode(self.windowSize)
        self.run = True
        self.Anton = Player()
        self.state = StartMenuState(self)
        self.state.init()

    def gameInit(self):
        self.eRoad=RoadEnemy()
        self.Fon=pg.image.load("5COGX.png")
        self.Fon_1 = pg.transform.scale(self.Fon, (700,700))
        self.deltatime = 2000
        self.onetime=0
        self.enemys=[]
        self.allTowers=[]
        self.Menus=[]
        self.buyMenu=Menu(150,150,(255,0,0),self.screen,self.Anton)
        self.buyMenu.addButton("Огн. башня",GS.RED,BF.buyFireTower)
        self.buyMenu.addButton("Лед. башня",GS.BLUE,BF.buyIceTower)
        self.buyMenu.addButton("Лаз. башня",GS.GREEN,BF.buyLazerTower)
        self.Menus.append(self.buyMenu)
        self.enemyHp=500
        self.lvlUpMenu = Menu(150,30,(255,0,0),self.screen,self.Anton)
        self.lvlUpMenu.addButton("Левел АП 30з",GS.BLUE,BF.lvlUp)
        self.Menus.append(self.lvlUpMenu)
        self.Anton.allTowers=[]
        self.Anton.gold = 50 
        self.Anton.livePoints = 20

    def drawGame(self,time): #Надо разбить на методы 
        self.screen.blit((self.Fon_1),(0,0))

        for i in range(len(self.enemys)-1): # проверка убийства врагов и очистка карты от них 
            if self.enemys[i].HP <= 0:
                del self.enemys[i]
                self.Anton.gold += 5        # Получение золота игроком за убийство врага
                print(self.Anton.gold,"+5")
            if self.enemys[i].x == self.eRoad.road[len(self.eRoad.road)-2][0] and self.enemys[i].y == self.eRoad.road[len(self.eRoad.road)-2][1] : #Проверяем врагов на конечной точке
                del self.enemys[i]                  # Удаляем и отнимаем очки,Если очки закончились
                self.Anton.lossLivePoints() # То Функция возвращает False в run whila

        for enemy in self.enemys: # действия и отрисовка врагов 
            enemy.go(self.eRoad.road,time)
            enemy.viewEnemy(time)

        for tower in self.Anton.allTowers: # действия и отрисовка башень
            tower.live(self.enemys,time)

        if self.deltatime <= time - self.onetime: # Появление врагов каждые deltatime(#нужно выделить отдельный метод)
            self.onetime = time
            SamyiStrawniiVrag1=Enemy(self.eRoad,self.screen,self.enemyHp)
            self.enemys.append(SamyiStrawniiVrag1)
            self.enemyHp += 25

        for menu in self.Menus: #Показ меню
            menu.viewMenu()
        self.viewScore()
        pg.display.update()

    def closeAllGameMenu(self):
        for menu in self.Menus:
            menu.inter = False
            
    def drawStartMenu(self,time):
        self.startMenu.viewMenu()
        pg.display.update()

    def drawFinishMenu(self,time):
        self.finishMenu.viewMenu()
        pg.display.update()

    def checkHotKey(self): #метод обработки нажатий для подставления в другие методы 
        self.press=False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.run=False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    coord = event.pos
                    button=3
                    self.press=True
                if event.button == 1:
                    coord=event.pos
                    button = 1
                    self.press=True
                return [coord,button,self.press]

    def inputMouseButtonInGame(self):
        input = self.checkHotKey()
        if self.press:
            if input[1] == 1: #input[1] это нажатая кнопка input[0] это координата
                self.buyMenu.selectButton(input[0])
                if self.Anton.hitTower(input[0]):
                    print("Пoпали по башне")
                    self.lvlUpMenu.addCoordinate(input[0])
                else: self.lvlUpMenu.selectButton(input[0])
            if input[1] == 3:
                perMenu = self.eRoad.blockSpawnUnit(input[0]) # проверяем чтобы мето не было на тропе врагов
                hitTower1 = self.Anton.hitTower(input[0])  # Проверяем что мы не ставим башню на башню 
                if perMenu and not hitTower1: 
                    self.buyMenu.addCoordinate(input[0])

    def inputMouseButtonInBigMenu(self):
        input = self.checkHotKey()
        if self.press:
            if input[2]:
                if input[1] == 1:
                    self.startMenu.selectButton(input[0])

    #def delAllUnit(self):
    #    self.enemys=[]
    #    self.Anton.allTowers=[]


    def buildStartMenu(self):
        self.startMenu=Menu(700,700,(255,0,0),self.screen,self.Anton)
        self.startMenu.addButton("                   Начать",GS.BLUE,BF.play) # сделаю(л) кнопку начала игры и всех кнопок стартового меню из методов игрока
        self.startMenu.addButton("                   Выйти",GS.BLUE,BF.quit)

    def buildFinishMenu(self):
        self.finishMenu=Menu(700,700,(255,0,0),self.screen, self.Anton)
        self.finishMenu.addButton("                   Повторить",GS.BLUE,BF.play)
        self.finishMenu.addButton("                    Выйти",GS.BLUE,BF.quit)
    
    def initAndStopStartMenu(self):
        self.startMenu.addCoordinate((0,0)) #вводим начальные координаты чтоб открыть меню

    def initAndStopFinishMenu(self):
        self.finishMenu.addCoordinate((0,0))
        print("инициализация меню")
    def draw(self,time):
        self.state.draw(time)

    def processEvents(self):
        self.state.processEvents()

    def changeState(self,newState):
        self.state = newState(self)
        self.state.init()

    def viewPauseMenu(self):
        pass

    def quit(self):
        pass

    def getRun(self):
        return self.run
        
    def viewScore(self):
        fontObj = pg.font.Font('18963.ttf', 20)
        text = str(self.Anton.gold)
        text1=str(self.Anton.livePoints)
        textSurfaceObj = fontObj.render((f"Золото: {text} Очки: {text1}") , False, GS.BLUE, GS.GREEN) # Вывод табло очков и золота
        self.screen.blit(textSurfaceObj,(250,50))
