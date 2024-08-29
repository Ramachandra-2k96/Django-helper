import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
red = (213, 50, 80)
black = (0, 0, 0)
green = (0, 128, 0)

dis_width = 600
dis_height = 400

disp = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    disp.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(disp, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    direction = 'right'
    change_to = 'right'

    snake_list = []
    Length = 1

    score = 0

    fruit_pos = [random.randrange(1, (dis_width // 10)) * 10,
                 random.randrange(1, (dis_height // 10)) * 10]
    fruit_spawn = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'right':
                    change_to = 'left'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    change_to = 'right'
                elif event.key == pygame.K_UP and direction != 'down':
                    change_to = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    change_to = 'down'

        head = [dis_width / 2,
                dis_height / 2]
        snake_list.append(head)

        if len(snake_list) > Length:
            del snake_list[0]

        body = []
        for x in snake_list[:-1]:
            body.append(x)
        snake_list[:] = body

        if head[0] == fruit_pos[0] and head[1] == fruit_pos[1]:
            score += 1
            length += 1
            fruit_spawn = False

        

        if change_to == 'left':
            head[0] -= snake_block
        elif change_to == 'right':
            head[0] += snake_block
        elif change_to == 'up':
            head[1] -= snake_block
        elif change_to == 'down':
            head[1] += snake_block

        disp.fill(green)

        our_snake(snake_block, snake_list)

        if head[0] < 0 or head[0] > dis_width - snake_block:
            message("Game Over!", red)
            pygame.display.update()
            time.sleep(2)
            quit()

        elif head[1] < 0 or head[1] > dis_height - snake_block:
            message("Game Over!", red)
            pygame.display.update()
            time.sleep(2)
            quit()

        elif head in snake_list[:-1]:
            message("Game Over!", red)
            pygame.display.update()
            time.sleep(2)
            quit()

        if fruit_spawn == False:
            fruit_pos = [random.randrange(1, (dis_width // 10)) * 10,
                         random.randrange(1, (dis_height // 10)) * 10]

        fruit_spawn = True

        your_score(score)

        pygame.display.update()
        clock.tick(snake_speed)
        snake_list.append(head)

gameLoop()