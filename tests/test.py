import pygame, sys
from pygame.locals import *

pygame.init()

ammo = "10" # you have ten ammo, use it wisely...

WIDTH = 600
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Bomber')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKBLUE = (2, 9, 129)
YELLOW = (255, 255, 255)

SCREEN.fill(DARKBLUE)
pygame.display.flip()
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Bomber', True, (255, 0, 0), (255, 255, 255))
dest = (100, 100)
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    SCREEN.blit(text, dest)
    pygame.display.flip()

pygame.quit()