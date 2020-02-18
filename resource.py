import pygame

WIDTH = 1280
HEIGHT = 860
cube_size = 20
cube = pygame.Surface((cube_size, cube_size))
cube.fill((205, 10, 88))
Foodcolor = (205, 10, 88)
Snakecolor = (255, 255, 255)
food = None
foodlist = []
food_number = 20
snake = None

background = None
myFont = None

obstaclelist = []
obstacle_number = 0
obstacle_color = (100,100,100)
speed = 5

game_time = 0.0
stop_time = 50
game_start = True
cross_side_mode = True
overlap_mode = False
timing_mode = True