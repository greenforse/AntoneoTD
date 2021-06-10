import pygame as pg
from RoadEnemy import RoadEnemy

pg.init()
clock=pg.time.Clock()
fps=10
windowSize=(700,700)
backGround=(50,30,100)
screen = pg.display.set_mode(windowSize)
screen.fill(backGround)
r1=pg.draw.rect(screen,(255,0,0),(300,0,50,500))
r2=pg.draw.rect(screen,(255,0,0),(300,450,400,50))
pg.display.update()

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run=False
    clock.tick(fps)

