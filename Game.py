
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
        self.buyMenu=Menu(200,200,(255,0,0),self.screen,self.Anton)
        self.buyMenu.addButton("Огн. башня: 20з.",GS.RED,BF.buyFireTower,24)
        self.buyMenu.addButton("Лед. башня: 20з.",GS.BLUE,BF.buyIceTower,24)
        self.buyMenu.addButton("Лаз. башня: 20з.",GS.GREEN,BF.buyLazerTower,24)
        self.Menus.append(self.buyMenu)
        self.enemyHp=500
        self.lvlUpMenu = Menu(150,30,(255,0,0),self.screen,self.Anton)
        self.lvlUpMenu.addButton("Левел АП 20з",GS.BLUE,BF.lvlUp,24)
        self.Menus.append(self.lvlUpMenu)
        self.Anton.refresh()
        self.fontObj = pg.font.Font('18963.ttf', 20)
        self.wave = 1
        self.countEnemy=0
        self.enemyToChangeWave=20
        self.oneTimeWavePause=0
        self.pauseDeltaTime=10000
        self.pause = False
        self.bustHPEnemy = 25
        #self.Anton.gold = 50 #сделать метод
        #self.Anton.livePoints = 20#сделать метод

    def drawGame(self,time): #Надо разбить на методы 
        self.screen.blit((self.Fon_1),(0,0))
        
        if len(self.enemys)>0:
            for i in range(len(self.enemys)):
                #print(i,) # проверка убийства врагов и очистка карты от них !!!!(было лен-1)
                if self.enemys[i-1].HP <= 0:
                    del self.enemys[i-1]
                    self.Anton.gold += 5        # Получение золота игроком за убийство врага
                    print(self.Anton.gold,"+5")
            for i in range(len(self.enemys)):
                if self.enemys[i-1].x == self.eRoad.road[len(self.eRoad.road)-2][0] and self.enemys[i-1].y == self.eRoad.road[len(self.eRoad.road)-2][1] : #Проверяем врагов на конечной точке
                    del self.enemys[i-1]                  # Удаляем и отнимаем очки,Если очки закончились
                    self.Anton.lossLivePoints()
                    return # То Функция возвращает False в run whila
        for enemy in self.enemys: # действия и отрисовка врагов 
            enemy.go(self.eRoad.road,time)
            enemy.viewEnemy(time)

        for tower in self.Anton.allTowers: # действия и отрисовка башень
            tower.live(self.enemys,time)

        self.spawnEnemy(time)
        #if self.deltatime <= time - self.onetime: # Появление врагов каждые deltatime(#нужно выделить отдельный метод)
        #    self.onetime = time
        #    SamyiStrawniiVrag1=Enemy(self.eRoad,self.screen,self.enemyHp)
        #    self.enemys.append(SamyiStrawniiVrag1)
        #    self.enemyHp += 25
        pg.draw.rect(self.screen,(138,0,0),(500,280, 200,70))
        for menu in self.Menus: #Показ меню
            menu.viewMenu()
        self.viewScore()
        pg.display.update()

    def spawnEnemy(self,time):
        if not self.pause:
            if self.deltatime <= time - self.onetime and self.countEnemy <= self.enemyToChangeWave: # Появление врагов каждые deltatime(#нужно выделить отдельный метод)
                self.onetime = time
                SamyiStrawniiVrag1=Enemy(self.eRoad,self.screen,self.enemyHp)
                self.enemys.append(SamyiStrawniiVrag1)
                self.enemyHp += self.bustHPEnemy
                self.countEnemy+=1
        if self.countEnemy >=self.enemyToChangeWave and len(self.enemys) == 0:
            self.changeWave(time)
        self.checkWavePause(time)
    def changeWave(self,time):
        self.countEnemy=0
        self.wave += 1
        self.deltatime -= 400
        self.bustHPEnemy += 10
        self.enemyToChangeWave+=20
        self.wavePause=True
        self.oneTimeWavePause=time
        self.pause = True

    def checkWavePause(self,time):
        if self.pauseDeltaTime <= time - self.oneTimeWavePause:
            self.pause=False




    def closeAllGameMenu(self):
        for menu in self.Menus:
            menu.interFalse()
            
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
                    self.startMenu.selectButtonInMenu(input[0])

    #def delAllUnit(self):
    #    self.enemys=[]
    #    self.Anton.allTowers=[]


    def buildStartMenu(self):
        self.startMenu=Menu(700,700,(255,0,0),self.screen,self.Anton)
        self.startMenu.addButton("                       Начать",(138,0,0),BF.play,38) # сделаю(л) кнопку начала игры и всех кнопок стартового меню из методов игрока
        self.startMenu.addButton("                       Выйти",GS.BLUE,BF.quit,38)

    def buildFinishMenu(self):
        self.finishMenu=Menu(700,700,(255,0,0),self.screen, self.Anton)
        self.finishMenu.addButton("                    Повторить",(0,139,139),BF.play,50)
        self.finishMenu.addButton("                    Выйти",GS.BLUE,BF.quit,50)
    
    def initAndStopStartMenu(self):
        self.startMenu.addCoordinate((0,0)) #вводим начальные координаты чтоб открыть меню

    def initAndStopFinishMenu(self):
        self.finishMenu.addCoordinate((0,0))
        print("инициализация меню",self.finishMenu.inter)
        pg.display.update()
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
        text = str(self.Anton.gold)
        text1=str(self.Anton.livePoints)
        text2=str(self.wave)
        textSurfaceObj = self.fontObj.render((f"Золото: {text} Очки: {text1} Волна:{text2}") , False, GS.BLUE, GS.GREEN) # Вывод табло очков и золота
        self.screen.blit(textSurfaceObj,(250,50))
