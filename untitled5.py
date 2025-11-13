# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 06:39:51 2022

@author: RIYA
"""

import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")
background=pygame.image.load("bg.jpg").convert()
y1=25
velocity=0.1
y2=475



while True:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
               pygame.quit()      
    
    
    
    
    
    
    y1=y1+velocity
    y2=y2+velocity
    if y1>=590:
        velocity=-velocity
    if y1<=1:
        velocity=-velocity
    if y2>=590:
        velocity=-velocity
    if y2<=30:
        velocity=+velocity
    screen.blit(background,(0,0))
    pygame.draw.circle(screen,WHITE ,(150,y1),15)
    pygame.draw.circle(screen,WHITE ,(250,y2),15)
    pygame.display.update()
    
