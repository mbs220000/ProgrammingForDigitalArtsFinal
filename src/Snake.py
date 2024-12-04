#Import Pygame
import random
import pygame

#Set Window Size/ Popup Screen
def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        pygame.display.flip()
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