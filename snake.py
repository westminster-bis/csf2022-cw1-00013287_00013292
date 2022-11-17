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