
import pygame as pg
from Game import Game
tDGame=Game()
pg.init()
while tDGame.run:
    time=pg.time.get_ticks()
    tDGame.processEvents()
    tDGame.draw(time)
    
