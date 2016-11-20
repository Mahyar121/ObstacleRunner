import pygame

# game options
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
title = "Obstacle Runner"
clock = pygame.time.Clock()
FPS = 60
FONTNAME = "AntsyPants.ttf"
spritesheetPlatformFile = "spritesheet_platforms.png"
playerspritesheetFile = "p1_walk.png"
# global vector
vector2 = pygame.math.Vector2

# Player Properties
playerAcceleration = 0.5
playerFriction = -0.12
playerGravity = 0.8
playerJump = 20

# colors
white = (255, 255, 255)
blue = (0, 0, 255)
teal = (0, 200, 255)
green = (0, 200, 0)
brightGreen = (0, 255, 0)
pink = (240, 108, 227)
red = (255, 0, 0)
yellow = (255, 252, 124)
black = (0, 0, 0)
orange = (255, 125, 0)
brightOrange = (255, 190, 0)
lightPurple = (216, 191, 216)