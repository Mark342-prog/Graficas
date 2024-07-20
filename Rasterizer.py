import pygame
from pygame.locals import *
from gl import renderer
    
width = 960
height = 540


screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

rend = renderer(screen)
rend.glColor(1,0,1)



def fill(surface, position):
        fill_color = rend.glColor(1,1,1) 
        surf_array = pygame.surfarray.pixels2d(surface)  
        current_color = surf_array[position]  
        frontier = [position]
        while len(frontier) > 0:
            x, y = frontier.pop()
            try: 
                if surf_array[x, y] != current_color:
                    continue
            except IndexError:
                continue
            surf_array[x, y] = fill_color
          
            frontier.append((x + 1, y)) 
            frontier.append((x - 1, y))  
            frontier.append((x, y + 1))  
            frontier.append((x, y - 1))  

        pygame.surfarray.blit_array(surface, surf_array)


isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
                
    punto0 = (width/2, height/2)
    #estrella
    rend.gLine((165, 380),(185, 360))
    rend.gLine((185, 360),(180, 330))
    rend.gLine((180, 330),(207, 345))
    rend.gLine((207, 345),(233, 330))
    rend.gLine((233, 330),(230, 360))
    rend.gLine((230, 360),(250, 380))
    rend.gLine((250, 380),(220, 385))
    rend.gLine((220, 385),(205, 410))
    rend.gLine((205, 410),(193, 383))
    rend.gLine((165, 380),(193, 383))
    #Poligono
    #(321, 335) (288, 286) (339, 251) (374, 302)
    rend.gLine((321, 335), (288, 286))
    rend.gLine((288, 286), (339, 251))
    rend.gLine((339, 251), (374, 302))
    rend.gLine((374, 302), (321, 335))
    #Poligono
    #(377, 249) (411, 197) (436, 249)
    rend.gLine((377, 249),(411, 197))
    rend.gLine((411, 197), (436, 249))
    rend.gLine((436, 249), (377, 249))
    #tetera
    # (413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215) , (552, 214), (517, 144), (466, 180),
    
    rend.gLine((413, 177), (448, 159))
    rend.gLine((448, 159), (502, 88))
    rend.gLine((502, 88), (553, 53))
    rend.gLine((553, 53), (535, 36))
    rend.gLine((535, 36), (676, 37))
    rend.gLine((676, 37), (660, 52))
    rend.gLine((660, 52), (750, 145))
    rend.gLine((750, 145), (761, 179))
    rend.gLine((761, 179), (672, 192))
    rend.gLine((672, 192), (659, 214))
    rend.gLine((659, 214), (615, 214))
    rend.gLine((632, 230), (615, 214))
    rend.gLine((632, 230), (580, 230))
    rend.gLine((580, 230), (597, 215))
    rend.gLine((597, 215), (552, 214))
    rend.gLine((552, 214), (517, 144))
    rend.gLine((517, 144), (466, 180))
    rend.gLine((466, 180), (413, 177))
    #
    #(682, 175), (708, 120), (735, 148), (739, 170),
    rend.gLine((682, 175), (708, 120))
    rend.gLine((708, 120), (735, 148))
    rend.gLine((735, 148), (739, 170))
    rend.gLine((739, 170), (682, 175))
    
    fill(rend,(682, 175))
    

    pygame.display.flip()
    clock.tick(60)
    
    
pygame.quit()
