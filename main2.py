
import pygame as pg
from Game import Game
tDGame=Game()
pg.init()
run = tDGame.getRun()
while run:
    tDGame.processEvents()
    tDGame.draw(pg.time.get_ticks())
    run = tDGame.getRun()
