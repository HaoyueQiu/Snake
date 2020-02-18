from resource import *


class Food:

    # 可以直接在创建的时候就随机
    # 食物的初始化，x，y食物的位置
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


class Snake:
    def __init__(self,cross_side_mode,overlap_mode):

        self.body = [[100, 100], [120, 100], [140, 100]]
        self.head = [140, 100]
        self.moving_direction = 'right'
        self.speed = 4
        self.color = (255, 255, 255)
        self.eat_food = False
        self.game_start = True
        self.is_cross_side = cross_side_mode
        self.is_overlap = overlap_mode

    def move(self):
        if self.eat_food:
            self.eat_food = False
        else:
            self.body.pop(0)

        if self.moving_direction == 'right':
            self.head[0] += cube_size
        elif self.moving_direction == 'left':
            self.head[0] -= cube_size
        elif self.moving_direction == 'up':
            self.head[1] -= cube_size
        elif self.moving_direction == 'down':
            self.head[1] += cube_size

        self.body.append(self.head.copy())

    def cross_side(self):
        if self.head[0] >= WIDTH:
            self.head[0] = self.head[0] - WIDTH
        if self.head[0] < 0:
            self.head[0] = self.head[0] + WIDTH
        if self.head[1] >= HEIGHT:
            self.head[1] = self.head[1] - HEIGHT
        if self.head[1] < 0:
            self.head[1] = self.head[1] + HEIGHT
        self.body.pop()
        self.body.append(self.head.copy())

    def game_over_cross(self):
        '''当蛇碰到边缘时判定游戏结束'''
        if self.head[0] < 0 or self.head[0] > WIDTH or \
                self.head[1] < 0 or self.head[1] > HEIGHT:
            self.game_start = False

    def game_over_overlap(self):
        '''当蛇的身子有重叠时判定为游戏结束'''
        if self.body.count(self.head) > 1:
            self.game_start = False

    # def change_direction(self, key):
    #     directions = [['up', 'down'], ['left', 'right']]
    #     if self.moving_direction in directions[0] and key in directions[1]:
    #         self.moving_direction = key
    #     elif self.moving_direction in directions[1] and key in directions[0]:
    #         self.moving_direction = key
    #
    #     # 判断游戏是否结束，即蛇是否碰到自身或是撞到墙壁


class Button:
    def __init__(self, color, w, h, x, y, text):
        self.color = color
        self.text = text
        self.x = x
        self.y = y
        self.image = pygame.Surface((w, h))
