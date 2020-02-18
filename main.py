import pygame
from resource import *
from pygame.locals import *
from element import *
from random import *
import sys


def createFood():
    global Foodcolor, foodlist, food, cube_size
    food = Food(Foodcolor, (randint(0, WIDTH) // cube_size) * cube_size, (randint(0, HEIGHT) // cube_size) * cube_size)
    foodlist.append(food)

def eat_food():
    pass

def touch_obstacle():
    global obstaclelist,snake
    for i in obstaclelist:
        if snake.head == [i.x,i.y]:
            return True
    return False

# initialization 初始化，用来生成各种基本元素
def initGame():
    global Foodcolor, food, food_number, snake, background,myFont
    global obstacle_number,obstaclelist,obstacle_color
    global cross_side_mode,overlap_mode,game_time
    game_time = 0
    pygame.init()
    '''创建food range(10) [0,1,2,3,4,5,6,7,8,9]'''
    for i in range(food_number):
        createFood()

    snake = Snake(cross_side_mode,overlap_mode)

    background = pygame.Surface((WIDTH, HEIGHT))
    # RGB (0,0,0) black  (255,255,255) white
    # surface.fill(())
    background.fill((0, 0, 0))

    # background = pygame.Surface((WIDTH, HEIGHT))
    # background.fill((0, 0, 0))
    # food = Food(Foodcolor,randint(0,WIDTH),randint(0,HEIGHT))

    myFont = pygame.font.SysFont(None,30)

    for i in range(obstacle_number):
        obstacle = Food(obstacle_color, (randint(0, WIDTH) // cube_size) * cube_size,
                    (randint(0, HEIGHT) // cube_size) * cube_size)
        obstaclelist.append(obstacle)


def updateLogic():
    global snake, foodlist,food_number,game_time,timing_mode
    global health_point,delay_time
    for i in range(food_number):
        # if [foodlist[i].x, foodlist[i].y] in snake.body:

        for j in snake.body:
            if [foodlist[i].x, foodlist[i].y] == j:
                snake.eat_food = True
                foodlist.pop(i)
                createFood()
    snake.move()
    if snake.is_cross_side:
        snake.cross_side()
    else:
        snake.game_over_cross()

    if snake.is_overlap == False:
        snake.game_over_overlap()
    game_time += delay_time/1000
    if timing_mode and game_time >= stop_time:
        snake.game_start = False
    if touch_obstacle():
        health_point -= 1
    if health_point == 0:
        snake.game_start = False


def updateView(screen):
    global cube, food, foodlist, food_number, snake, background,myFont
    global obstaclelist,obstacle_color,obstacle_number,game_time,health_point

    # surface1.blit(surface2,location)
    screen.blit(background, ([0, 0]))

    cube.fill(food.color)

    for i in range(food_number):
        screen.blit(cube, (foodlist[i].x, foodlist[i].y))

    cube.fill(snake.color)
    # for i in [[100,100],[120,100],[140,100]]
    # [100,100]
    # [120,100]
    # [140,100]
    for i in snake.body:
        screen.blit(cube, (i[0], i[1]))

    testSur = myFont.render('score: %d' % (len(snake.body)-3),True,(255,255,255))
    screen.blit(testSur,[10,10])

    testSur = myFont.render('time: %ds' % int(game_time), True, (255, 255, 255))
    screen.blit(testSur, [120, 10])

    testSur = myFont.render('HP: %d' % health_point, True, (255, 255, 255))
    screen.blit(testSur, [220, 10])
    # screen.blit(cube,(food.x,food.y))
    cube.fill(obstacle_color)
    for i in range(obstacle_number):
        screen.blit(cube,(obstaclelist[i].x,obstaclelist[i].y))

def mainLoop():
    global snake,delay_time
    initGame()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    while True:
        # pygame.time.delay(延迟的时间，单位是毫秒)
        # pygame.time.delay(int(400/snake.speed))
        # delay_time = 100
        pygame.time.delay(delay_time)

        # pygame.event.get() 获取事件队列
        for event in pygame.event.get():
            # type判断事件类型
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # key告诉你按下的键是哪一个 K_a K_b K_c
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_w or event.key == K_UP:
                    if snake.moving_direction == 'right' or snake.moving_direction == 'left':
                        snake.moving_direction = 'up'
                elif event.key == K_s or event.key == K_DOWN:
                    if snake.moving_direction == 'right' or snake.moving_direction == 'left':
                        snake.moving_direction = 'down'
                elif event.key == K_a or event.key == K_LEFT:
                    if snake.moving_direction == 'up' or snake.moving_direction == 'down':
                        snake.moving_direction = 'left'
                elif event.key == K_d or event.key == K_RIGHT:
                    if snake.moving_direction == 'up' or snake.moving_direction == 'down':
                        snake.moving_direction = 'right'
                elif event.key == K_SPACE:
                    if snake.game_start == False:
                        initGame()
                        snake.game_start = True

        if snake.game_start == True:
            updateLogic()
            updateView(screen)
            pygame.display.flip()


if __name__ == '__main__':
    mainLoop()
