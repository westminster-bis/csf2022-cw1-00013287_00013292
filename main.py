import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 1280
dis_height = 720

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by 00013287 & 00013292')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("verdana", 25)
score_font = pygame.font.SysFont("verdana", 35)