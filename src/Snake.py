#Import Pygame
import pygame

#Set Window Size/ Popup Screen
pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()



#class Snake():

    #def snakespawn():
#class Fruit():
    #def fruitspawn():

#Spawn Snake

#Spawn Fruit/ Despawn

#Scores?/ Gameover

#Movement (Wasd)

#Snake Grows