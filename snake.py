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

# define a function for displaying in-game score
def show_game_score(font, size, game_score):
    game_score_font = pygame.font.SysFont(font, size);
    game_score_surface = game_score_font.render((player_name + "'s Game Score: " + str(game_score)), True, white)
    game_score_rect = game_score_surface.get_rect()
    game_score_rect.midtop = (display_height, 15)
    win.blit(game_score_surface, game_score_rect)

# define a function for displaying generated collision object
def show_collision_obj(collision_obj_position, snake_width, snake_height):
    collision_obj_rect = pygame.Rect(collision_obj_position[0], collision_obj_position[1], snake_width, snake_height)
    collision_obj_image = pygame.image.load("./red-brick-wall.jpg")
    collision_obj_image_resize = pygame.transform.scale(collision_obj_image, (snake_width, snake_height))
    win.blit(collision_obj_image_resize, collision_obj_rect)

# define a function for assinging a name to a player
def set_player_name(name):
    global player_name;
    global default_player_name;
    player_name = name;
    default_player_name = False;

# define a function for setting default name to user
def set_default_player_name():
    global player_name;
    global default_player_name;
    player_name = "Guest";
    default_player_name = False;