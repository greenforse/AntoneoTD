from Menu import Menu
from RoadEnemy import RoadEnemy
import pygame as pg
from Player import Player
import GameSetup as GS
import ButtonFunction as BF

class Game():

    def _init_(self):
        self.eRoad=RoadEnemy()
        self.clock=pg.time.Clock()
        self.windowSize=(700,700)
        self.screen = pg.display.set_mode(self.windowSize)
        self.Fon=pg.image.load("5COGX.png")
        self.Fon_1 = pg.transform.scale(self.Fon, (700,700))
        self.RED=(255,0,0)
        self.BLUE=(0,0,255)
        self.GREEN=(0,255,0)
        self.run = True
        #self.#SamyiStrawniiVrag1=Enemy(eRoad,screen)
        self.enemys=[]
        #self.#enemys.append(SamyiStrawniiVrag1)
        self.allTowers=[]
        self.Anton = Player()
        self.deltatime = 2000
        self.onetime=0
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
        self.startMenu=Menu(700,700,(255,0,0),self.screen,self.Anton)
        self.startMenu.addButton("Начать",GS.BLUE,BF.lvlUp)
        self.startMenu.addButton("Выйти",GS.BLUE,BF.lvlUp)
        self.state = None# Потом добавить статус
        self.play = True

    def drawGame(self,time):
        self.screen.blit((self.Fon_1),(0,0))

        for i in range(len(self.enemys)-1): # проверка убийства врагов и очистка карты от них 
            if self.enemys[i].HP <= 0:
                del self.enemys[i]
                self.Anton.gold += 5        # Получение золота игроком за убийство врага
                print(self.Anton.gold,"+5")
            if self.enemys[i].x == self.eRoad.road[len(self.eRoad.road)-2][0] and self.enemys[i].y == self.eRoad.road[len(self.eRoad.road)-2][1] : #Проверяем врагов на конечной точке
                del self.enemys[i]                  # Удаляем и отнимаем очки,Если очки закончились
                self.play = self.Anton.lossLivePoints() # То Функция возвращает False в run whila

        for enemy in self.enemys: # действия и отрисовка врагов 
            enemy.go(self.eRoad.road,time)
            enemy.viewEnemy(time)

        for tower in self.Anton.allTowers: # действия и отрисовка башень
            tower.live(self.enemys,time)

        if self.deltatime <= time - self.onetime: # Появление врагов каждые deltatime
            self.onetime = time
            SamyiStrawniiVrag1=self.Enemy(self.eRoad,self.screen,self.enemyHp)
            self.enemys.append(SamyiStrawniiVrag1)
            self.enemyHp += 25

        for menu in self.Menus: #Показ меню
            menu.viewMenu()
        self.viewScore()
        pg.display.update()

    def draw(self,time):
        self.state.draw(time)

    #def inputMouseButton(self,coord,button):
    #    if button == 1:
    #        self.buyMenu.selectButton(coord)
    #        if self.Anton.hitTower(coord):
    #            print("Папали по башне")
    #            self.lvlUpMenu.addCoordinate(coord)
    #        else: self.lvlUpMenu.selectButton(coord)
    #    if button == 3:
    #        perMenu = self.eRoad.blockSpawnUnit(coord) # проверяем чтобы мето не было на тропе врагов
    #        hitTower1 = self.Anton.hitTower(coord)  # Проверяем что мы не ставим башню на башню 
    #        if perMenu and not hitTower1: 
    #            self.buyMenu.addCoordinate(coord)

    def processEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.run=False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    coord = event.pos
                    perMenu = self.eRoad.blockSpawnUnit(coord) # проверяем чтобы мето не было на тропе врагов
                    hitTower1 = self.Anton.hitTower(coord)  # Проверяем что мы не ставим башню на башню 
                    if perMenu and not hitTower1: 
                        self.buyMenu.addCoordinate(coord)
                if event.button == 1:
                    cel=event.pos
                    self.buyMenu.selectButton(cel)
                    if self.Anton.hitTower(cel):
                        print("Папали по башне")
                        self.lvlUpMenu.addCoordinate(cel)
                    else: self.lvlUpMenu.selectButton(cel)

    def DrawStartMenu(self):
        self.startMenu.addCoordinate((0,0)) #вводим начальные координаты чтоб открыть меню
        self.startMenu.viewMenu()

    def vievPauseMenu(self):
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
