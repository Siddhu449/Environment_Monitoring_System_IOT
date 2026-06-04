import subprocess
import sys
import pygame
import time
import random

# Check if pygame is installed, if not, install it
try:
    import pygame
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    print("Pygame has been installed successfully!")

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (169, 169, 169)

# Screen dimensions
width = 800
height = 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10

# Load images
snake_img = pygame.Surface((snake_block, snake_block))
snake_img.fill(green)
food_img = pygame.Surface((snake_block, snake_block))
food_img.fill(yellow)

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 40)
score_font = pygame.font.SysFont("comicsansms", 30)

# Function to display the score
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [10, 10])

# Function to draw the snake
def our_snake(snake_List):
    for segment in snake_List:
        dis.blit(snake_img, (segment[0], segment[1]))

# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

# Function for the game loop
def gameLoop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Movement
    x1_change = 0
    y1_change = 0

    # Snake body and initial length
    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            dis.fill(gray)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for wall collision
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        dis.blit(food_img, (foodx, foody))

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        # Draw snake and score
        our_snake(snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

            # Increase snake speed as it grows
            if Length_of_snake % 5 == 0:
                global snake_speed
                snake_speed += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
