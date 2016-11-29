import pygame

# game options
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
title = "Obstacle Runner"
clock = pygame.time.Clock()
FPS = 60
FONTNAME = "AntsyPants.ttf"

# spritesheet files
spritesheetPlatformFile = "spritesheet_platforms.png"
# playerspritesheetFile = "p1_walk.png"
playerspritesheetFile = "Old hero.png"
coinsspritesheetFile = "coins.png"
enemyspritesheetFile = "spritesheet_platforms.png"

# global vector
vector2 = pygame.math.Vector2

# Player Properties
playerAcceleration = 0.5
playerFriction = -0.12
playerGravity = 0.8
playerJump = 20

# Game Properties
COIN_VALUE = 50
GOLD_COIN_SPAWN_RATE = 10
SILVER_COIN_SPAWN_RATE = 30
BRONZE_COIN_SPAWN_RATE = 50
ENEMYFLY_SPAWN_RATE = 5000
ENEMYFLY_SPEED = 3
ENEMYSPIKE_SPAWN_RATE = 50
ENEMYSPIKE_SPEED = 1
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
COIN_LAYER = 1
ENEMY_LAYER = 2
CLOUD_LAYER = 0

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
graypink = (157, 142, 135)
darkred = (251, 9, 9)