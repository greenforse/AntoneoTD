from Player import Player
from FireTower import FireTower
from Enemy import Enemy
import pygame as pg
from RoadEnemy import RoadEnemy
#from Enemy import Enemy

eRoad=RoadEnemy()
pg.init()
clock=pg.time.Clock()
windowSize=(700,700)
screen = pg.display.set_mode(windowSize)
Fon=pg.image.load("5COGX.png")
Fon_1 = pg.transform.scale(Fon, (700,700))
RED=(255,0,0)
run = True
SamyiStrawniiVrag1=Enemy(eRoad,screen)
enemys=[]
enemys.append(SamyiStrawniiVrag1)
allTowers=[]
Anton = Player()
deltatime = 2000
onetime=0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run=False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pg.draw.circle(screen, RED, event.pos, 10)
                cel=event.pos
                per = eRoad.blockSpawnUnit(cel) # проверяем чтобы мето не было на тропе врагов 
                if per:                         # если не стоит то  стоавим башню
                    NewTower=FireTower(10,100,cel,screen)
                    buyTower = Anton.buyTower(NewTower.price) #Проверяем наличие золота у игрока и снимаем его 
                    if buyTower:
                        print("-20",Anton.gold)
                        allTowers.append(NewTower)
                        print(cel)
                        pg.display.update()
                    else: print("Нету денюшек")
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
        enemy.go(eRoad.road,pg.time.get_ticks())
        enemy.viewEnemy(pg.time.get_ticks())

    for tower in allTowers: # действия и отрисовка башень
        tower.live(enemys,pg.time.get_ticks())
        
    if deltatime <= pg.time.get_ticks() - onetime: # Появление врагов каждые deltatime
        onetime = pg.time.get_ticks()
        SamyiStrawniiVrag1=Enemy(eRoad,screen)
        enemys.append(SamyiStrawniiVrag1)

    pg.display.update()
