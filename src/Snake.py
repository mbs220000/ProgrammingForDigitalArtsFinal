
import pygame
import random
import time

pygame.init()

distance_x, distance_y = 800, 600
screen = pygame.display.set_mode((distance_x, distance_y))
pygame.display.set_caption("Snake Game")

#Basic Colors
Black = pygame.Color (0, 0, 0)
White = pygame.Color (255, 255, 255)
Red = pygame.Color (255, 0, 0)
Green = pygame.Color (0, 255, 0)
Blue = pygame.Color (0, 0, 255)
Grey = pygame.Color (128,128,128)

#My Colors
PrettyRed = pygame.Color (170, 50, 50)
PrettyGrey = pygame.Color (140, 145, 140)
PrettyBlue = pygame.Color (50, 130, 170)


clock = pygame.time.Clock()

#Spawn Snake
snake_size = 40 #must be divisible by 10? for grid
snake_speed = 15
snake_head = [400, 300]
snake_body = [[300, 300],
              [200, 300],
              [100, 300]]
snake_direction = 'right'
change_to = snake_direction


def snake(snake_size, snake_body):
    for x in reversed (snake_body):
        pygame.draw.rect(screen, PrettyBlue, [x[0], x[1], snake_size, snake_size])
        #pygame.draw.rect(screen, Green, [x[0] + 1, x[1] + 1, snake_size - 2, snake_size - 2])
        
#Spawn/ Despawn Fruit
fruit_position = [random.randrange(1, distance_x // 10) * 10, 
                  random.randrange(1, distance_y // 10) * 10]

def fruit():
    #print(f"Fruit position: {fruit_position}")  # Check the fruit's position
    pygame.draw.rect(screen, PrettyRed, [fruit_position[0], fruit_position[1], snake_size, snake_size])

def game_score(score):
    value = score_font.render("Your Score:" + str(score), True, Black)
    screen.blit(value, [0, 0])

score_font = pygame.font.SysFont("times new roman", 25)

def game_over(score):
    end_score = score
    endscreen = end_score_font.render("Final Score:" + str(end_score), True, Black)
    game_end = endscreen.get_rect()
    game_end.midtop = (distance_x/2, distance_y/4)
    screen.blit(endscreen, game_end)
    pygame.display.flip() 
    time.sleep(3)
    pygame.quit()
    quit()

end_score_font = pygame.font.SysFont("times new roman", 40)


#Main Function fo running the game
def gameloop():
    global fruit_position, change_to, snake_direction
    score = 0
    fruit_spawn = True
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
            snake_head [1] -= snake_speed
        if snake_direction == 'down':
            snake_head [1] += snake_speed
        if snake_direction == 'left':
            snake_head [0] -= snake_speed
        if snake_direction == 'right':
            snake_head [0] += snake_speed

            
#Snake Body moves with Head and Snake grows
        snake_body.insert(0, list(snake_head))
            #Collider on fruit is bigger so you can just touch it and eat it
        if abs(snake_head[0] - fruit_position[0]) < snake_size and abs(snake_head[1] - fruit_position[1]) < snake_size:
            score += 1
            fruit_spawn = False
                #Add 2 segments instead of 1 when eating fruit
            for _ in range(2):  
                snake_body.insert(0, list(snake_head))
          #won't grow unless it eats fruit  
        else:
            snake_body.pop() 
          #When fruit is eaten it despawns and a new one spawns  
        if not fruit_spawn:
            fruit_position = [random.randrange(1, distance_x // 10) * 10, 
                              random.randrange(1, distance_y // 10) * 10]
            fruit_spawn = True 
        for pos in snake_body:
            pygame.draw.rect(screen, Green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
            pygame.draw.rect(screen, White, pygame.Rect(fruit_position[0], fruit_position[1], snake_size, snake_size))
        
        
#Snake, Fruit, and Score on Screen spawn
        screen.fill(PrettyGrey)
        snake(snake_size, snake_body)
        fruit()
        game_score(score) #Shows Score While Playing

        
#Game Over
        if snake_head[0] < 0 or snake_head[0] > distance_x -10:
            game_over(score)
        if snake_head[1] < 0 or snake_head[1] > distance_y -10:
            game_over(score)


        pygame.display.update()
        clock.tick(snake_speed) #FPS

gameloop()




