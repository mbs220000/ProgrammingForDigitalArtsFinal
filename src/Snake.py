#Import Pygame
import pygame
import random

#Colors for Game
Black = pygame.Color (0, 0, 0)
White = pygame.Color (255, 255, 255)
Red = pygame.Color (255, 0, 0)
Green = pygame.Color (0, 255, 0)
Blue = pygame.Color (0, 0, 255)
Grey = pygame.Color (128,128,128)

#Set Window Size/ Popup Screen
distance_x = 500
distance_y = 400

pygame.init()
pygame.display.set_caption('Snake Game Final')
screen = pygame.display.set_mode((distance_x, distance_y))
clock = pygame.time.Clock() #ForFPS/ snake movement
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    screen.fill("grey")
    #Render Code Here?

#Spawn Snake
snake_size = 10
snake_speed = 15
snake_headposition = [100, 50]

# defining first 4 blocks of snake body
snake_bodyposition = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]


#Spawn/ Despawn Fruit
fruit_position = [random.randrange(1, (distance_x//10)) * 10, 
                  random.randrange(1, (distance_y//10)) * 10]
fruit_spawn = True

#Scores?/ Gameover

#Movement (Wasd)

#Snake Grows


pygame.display.flip()
clock.tick(snake_speed) #FPS
pygame.quit()
quit()

