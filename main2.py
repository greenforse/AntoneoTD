
import pygame as pg
from Game import Game
tDGame=Game()
pg.init()
while tDGame.run:
    tDGame.processEvents()
    tDGame.draw(pg.time.get_ticks())
    
