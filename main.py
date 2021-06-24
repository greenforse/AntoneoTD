from Enemy import Enemy
import pygame as pg
from RoadEnemy import RoadEnemy
#from Enemy import Enemy

eRoad=RoadEnemy()
pg.init()
clock=pg.time.Clock()
fps=15
windowSize=(700,700)
screen = pg.display.set_mode(windowSize)
Fon=pg.image.load("5COGX.png")
Fon_1 = pg.transform.scale(Fon, (700,700))
RED=(255,0,0)
run = True
SamyiStrawniiVrag1=Enemy(eRoad)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run=False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pg.draw.circle(screen, RED, event.pos, 10)
                cel=event.pos
                print(cel)
                pg.display.update()
    screen.blit((Fon_1),(0,0))
    pg.draw.circle(screen,RED,(SamyiStrawniiVrag1.x,SamyiStrawniiVrag1.y),SamyiStrawniiVrag1.radius)
    SamyiStrawniiVrag1.go(eRoad.road)
    pg.display.update()
    clock.tick(fps)

