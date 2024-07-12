import pygame
from pygame.locals import *
    
width = 960
height = 540

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
