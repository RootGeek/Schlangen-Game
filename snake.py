import pygame
import time
import random

pygame.init()

# Bildschirmgröße
screen_width = 600
screen_height = 600

# Farben
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Schlangen-Größe
block_size = 20
snake_speed = 15

# Schriftart
font_style = pygame.font.SysFont(None, 50)

def display_message(message, color, y_displace=0):
    mesg = font_style.render(message, True, color)
    game_display.blit(mesg, (screen_width / 2 - mesg.get_width() / 2, screen_height / 2 + y_displace))

def snake_game():
    game_over = False
    game_close = False

    snake_list = []
    length_of_snake = 1

    # Schlangenposition
    snake_x = screen_width / 2
    snake_y = screen_height / 2

    # Bewegung der Schlangen
    snake_x_change = 0
    snake_y_change = 0

    # Zufällige Position des Apfels
    apple_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    apple_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            game_display.fill(black)
            display_message("Du hast verloren!", red, y_displace=-50)
            display_message("Drücke Q zum Beenden", white, y_displace=50)
            display_message("oder", white, y_displace=80)
            display_message("C zum Neustarten", white, y_displace=110)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = block_size
                    snake_x_change = 0

        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        game_display.fill(black)

        # Zeichne das Gitter
        for x in range(0, screen_width, block_size):
            pygame.draw.line(game_display, white, (x, 0), (x, screen_height))
        for y in range(0, screen_height, block_size):
            pygame.draw.line(game_display, white, (0, y), (screen_width, y))

        pygame.draw.rect(game_display, green, [apple_x, apple_y, block_size, block_size])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(block_size, snake_list)
        pygame.display.update()

        if snake_x == apple_x and snake_y == apple_y:
            apple_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            apple_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], block_size, block_size])

if __name__ == "__main__":
    game_display = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Schlangenspiel')
    snake_game()
