import pygame
import pygame_menu
import random
import sys
from typing import Tuple, Any
from math import isclose

# initialize pygame
pygame.init()

# define display size
display_width = 600
display_height = 400

# define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# define initial difficulty level
difficulty = 0

# Game difficulty is assigned the following values:
#     Beginner = 25
#     Easy = 50
#     Medium = 100
#     Hard = 500

# set pygame display size
win = pygame.display.set_mode((display_width,display_height))
# set pygame window caption
pygame.display.set_caption('Snake Game by 00013287 & 00013292')
# set pygame clock for controlling in-game speed
clock = pygame.time.Clock()
# define player name
player_name = '';
# set default player name to True
default_player_name = True;

# define a function for generating snake food at random locations
def setup_snake_food():
    new_food_position = [random.randrange(1, (display_width//10))* 10, random.randrange(1, (display_height//10)) * 10]
    return new_food_position

# define a function for generating obstacles
def setup_collision_obj():
    new_collision_obj = [random.randrange(1, (display_width//10))* 10, random.randrange(1, (display_height//10)) * 10]
    return new_collision_obj

# define a function for setting up game difficulty
def set_game_difficulty(selected: Tuple, value: Any):
    if(value == 1):
        difficulty = 25
    elif(value == 2):
        difficulty = 50
    elif(value == 3):
        difficulty = 100
    elif(value == 4):
        difficulty = 500
    else:
        difficulty = 25