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
Black = pygame.Color (0, 0, 0)
White = pygame.Color (255, 255, 255)
Red = pygame.Color (255, 0, 0)
Green = pygame.Color (0, 255, 0)
Blue = pygame.Color (0, 0, 255)
Grey = pygame.Color (128,128,128)

# Clock
clock = pygame.time.Clock()

# Spawn Snake
snake_size = 25
snake_speed = 15
snake_head = [400, 300]
snake_body = [[400, 300],
              [425, 300],
              [450, 300],
              [475, 300]]
snake_direction = 'right'
change_to = snake_direction


def snake(snake_size, snake_grow):
    for x in snake_grow:
        pygame.draw.rect(screen, Black, [x[0], x[1], snake_size, snake_size])

# Spawn/ Despawn Fruit
fruit_position = [random.randrange(0, distance_x // snake_size) * snake_size, 
                      random.randrange(0, distance_y // snake_size) * snake_size]

def fruit():
    #print(f"Fruit position: {fruit_position}")  # Check the fruit's position
    pygame.draw.rect(screen, Red, [fruit_position[0], fruit_position[1], snake_size, snake_size])

def game_score(score):
    value = score_font.render("Your Score:" + str(score), True, Black)
    screen.blit(value, [0, 0])

score_font = pygame.font.SysFont("times new roman", 25)

def game_over():
    end_score = (snake_size - (snake_size-1))
    endscreen = end_score_font.render("Final Score:" + str(end_score), True, Black)
    game_end = endscreen.get_rect()
    game_end.midtop = (distance_x/2, distance_y/4)
    screen.blit(endscreen, game_end)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

end_score_font = pygame.font.SysFont("times new roman", 40)


# Main Function fo running the game
def gameloop():
    global fruit_position, change_to, snake_direction
    running = True
    #time.sleep(5)  # Add a delay to see if the loop starts
    while running:
        #print("Game loop running")  # Check if the loop is running
        for event in pygame.event.get():
            #print(event)  # Check if any events are detected
            if event.type == pygame.QUIT:
                running = False 

        #Moving the Snake
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'up'
                if event.key == pygame.K_DOWN:
                    change_to = 'down'
                if event.key == pygame.K_LEFT:
                    change_to = 'left'
                if event.key == pygame.K_RIGHT:
                    change_to = 'right'
        #Update snake direction
        if change_to == 'up' and snake_direction != 'down':
            snake_direction = 'up'
        if change_to == 'down' and snake_direction != 'up':
            snake_direction = 'down'
        if change_to == 'left' and snake_direction != 'right':
            snake_direction = 'left'
        if change_to == 'right' and snake_direction != 'left':
            snake_direction = 'right'
        #Move Snake
        if snake_direction == 'up':
            snake_head [1] -= 10
        if snake_direction == 'down':
            snake_head [1] += 10
        if snake_direction == 'left':
            snake_head [0] -= 10
        if snake_direction == 'right':
            snake_head [0] += 10
        #Snake Body moves with Head
        snake_body.insert(0, list(snake_head))
        if snake_head[0] == fruit_position[0] and snake_head[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
        

        #Snake, Fruit, and Score on Screen spawn
        screen.fill(Grey)
        snake(snake_size, snake_body)
        fruit()
        game_score(snake_size - (snake_size-1)) #Shows Score While Playing
    
        #Game Over
        if snake_head[0] < 0 or snake_head[0] > distance_x-10:
            game_over()
        if snake_head[1] < 0 or snake_head[1] > distance_y-10:
            game_over()


        pygame.display.update()
        clock.tick(snake_speed)  # FPS

gameloop()




