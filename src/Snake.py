#Import Pygame
import pygame
import random
import time

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

#Spawn Snake
snake_size = 10
snake_speed = 15
snake_position = [[100, 50]]

def snake(snake_size, snake_grow):
    for x in snake_grow:
        pygame.draw.rect(screen, Black, [x[0], x[1], snake_size, snake_size])

#Spawn/ Despawn Fruit
def fruit():
    fruit_position = [random.randrange(0, (distance_x - snake_size /10)) * 10, 
                    random.randrange(0, (distance_y - snake_size /10)) * 10]
    pygame.draw.rect(screen, Red, [fruit_position[0], fruit_position[1], snake_size, snake_size])

#Main Function
def gameloop():
    running = True
    time.sleep(1) # Add a delay to see if the loop starts
    while running:
        print("Game loop running") #Check if loop is running
        for event in pygame.event.get():
            print(event)  # Check the events being processed
            if event.type == pygame.QUIT:
                running = False 
        screen.fill(Grey)
        snake(snake_size, snake_position)
        fruit()

        pygame.display.update()
        clock.tick(snake_speed) #FPS

    pygame.quit()




