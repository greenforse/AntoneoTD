import ButtonFunction as BF
from Player import Player
from FireTower import FireTower
from Enemy import Enemy
import pygame as pg
from RoadEnemy import RoadEnemy
#from Enemy import Enemy
from Menu import Menu
eRoad=RoadEnemy()
pg.init()
clock=pg.time.Clock()
windowSize=(700,700)
screen = pg.display.set_mode(windowSize)
Fon=pg.image.load("5COGX.png")
Fon_1 = pg.transform.scale(Fon, (700,700))
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
run = True
SamyiStrawniiVrag1=Enemy(eRoad,screen)
enemys=[]
enemys.append(SamyiStrawniiVrag1)
allTowers=[]
Anton = Player()
deltatime = 2000
onetime=0
Menus=[]
buyMenu=Menu(150,250,(255,0,0),screen,Anton)
buyMenu.addButton("Огн. башня",RED,BF.buyFireTower)
buyMenu.addButton("Лед. башня",GREEN,BF.buyFireTower)
buyMenu.addButton("Лаз. башня",BLUE,BF.buyFireTower)
Menus.append(buyMenu)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run=False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                coord = event.pos
                perMenu = eRoad.blockSpawnUnit(coord) # проверяем чтобы мето не было на тропе врагов 
                if perMenu:
                    buyMenu.addCoordinate(coord)
            if event.button == 1:
                cel=event.pos
                buyMenu.selectButton(cel)
    time = pg.time.get_ticks()                #сделал паузу на время открытия меню
    screen.blit((Fon_1),(0,0))

    for i in range(len(enemys)-1): # проверка убийства врагов и очистка карты от них 
        if enemys[i].HP <= 0:
            del enemys[i]
            Anton.gold += 5        # Получение золота игроком за убийство врага
            print(Anton.gold,"+5")
        if enemys[i].x == eRoad.road[len(eRoad.road)-2][0] and enemys[i].y == eRoad.road[len(eRoad.road)-2][1] : #Проверяем врагов на конечной точке
            del enemys[i]                  # Удаляем и отнимаем очки,Если очки закончились
            run = Anton.lossLivePoints() # То Функция возвращает False в run whila
                                                                                                                    
    for enemy in enemys: # действия и отрисовка врагов 
        enemy.go(eRoad.road,time)
        enemy.viewEnemy(time)

    for tower in Anton.allTowers: # действия и отрисовка башень
        tower.live(enemys,time)
        
    if deltatime <= time - onetime: # Появление врагов каждые deltatime
        onetime = time
        SamyiStrawniiVrag1=Enemy(eRoad,screen)
        enemys.append(SamyiStrawniiVrag1)

    for menu in Menus: #Показ меню
        menu.viewMenu()

    fontObj = pg.font.Font('18963.ttf', 20)
    text = str(Anton.gold)
    text1=str(Anton.livePoints)
    textSurfaceObj = fontObj.render((f"Золото: {text} Очки: {text1}") , False, BLUE, GREEN) # Вывод табло очков и золота
    screen.blit(textSurfaceObj,(250,50))
    pg.display.update()
