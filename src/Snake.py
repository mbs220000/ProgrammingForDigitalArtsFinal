import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
distance_x, distance_y = 800, 600
screen = pygame.display.set_mode((distance_x, distance_y))
pygame.display.set_caption("Snake Game")

# Colors
Black = (0, 0, 0)
Red = (255, 0, 0)
Grey = (200, 200, 200)

# Clock
clock = pygame.time.Clock()

# Spawn Snake
snake_size = 20
snake_speed = 15
snake_position = [[100, 50]]

def snake(snake_size, snake_grow):
    for x in snake_grow:
        pygame.draw.rect(screen, Black, [x[0], x[1], snake_size, snake_size])

# Spawn/ Despawn Fruit
fruit_position = [random.randrange(0, distance_x // snake_size) * snake_size, 
                      random.randrange(0, distance_y // snake_size) * snake_size]
def fruit():
    #print(f"Fruit position: {fruit_position}")  # Check the fruit's position
    pygame.draw.rect(screen, Red, [fruit_position[0], fruit_position[1], snake_size, snake_size])

# Main Function
def gameloop():
    global fruit_position
    running = True
    #time.sleep(5)  # Add a delay to see if the loop starts
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        screen.fill(Grey)
        snake(snake_size, snake_position)
        fruit()

        if snake_position[0] == fruit_position:
            fruit_position = [random.randrange(0, int((distance_x - snake_size / 10)) * 10), 
                              random.randrange(0, int((distance_y - snake_size / 10)) * 10)]

        pygame.display.update()
        clock.tick(snake_speed)  # FPS

    pygame.quit()

# Start the game loop
gameloop()




