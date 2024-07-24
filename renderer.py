import pygame
from pygame.locals import *
from gl import renderer
from model import Model

from shaders import vertexShader
from model import Model
width = 960
height = 540


screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

rend = renderer(screen)
rend.vertexShader = vertexShader

modelo1 = Model("model.obj")

rend.models.append(modelo1)


isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    rend.glRender()
                



    pygame.display.flip()
    clock.tick(60)
    
    
pygame.quit()