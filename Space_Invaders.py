import pygame
from pygame.locals import *
import time
import random

# Set colors dictionary
colors = {
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255)
}

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("Space_Invaders\stars.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Space_Invaders\ufo.png")
pygame.display.set_icon(icon)

# Joystick code
#joysticks = []
#for i in range(pygame.joystick.get_count()):
#    joysticks.append(pygame.joystick.Joystick(i))
#    joysticks[-1].init()

# Player
playerImg = pygame.image.load("Space_Invaders\spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
playerVel = 0.1

# Enemy
enemyImg = pygame.image.load(r"Space_Invaders\blien.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.1
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load(r"Space_Invaders\bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0.1
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    # Draw player onto the screen; blit means draw
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    # Draw player onto the screen; blit means draw
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Sound
sound = pygame.mixer.Sound("Space_Invaders\music.mp3")
# sound.play()

# Game loop
run = True
while run:

    # Creates the background of the game using RGB coloring - Red, Green, Blue
    screen.fill(colors["Black"])
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Quits pygame if the window is closed
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        # If a keystroke is pressed, check whether it is right or left

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1 * playerVel
            if event.key == pygame.K_RIGHT:
                playerX_change = playerVel
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Changes the playerX when the arrow keys are pressed
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.1
        enemyY += enemyY_change

    # Call player function
    player(playerX, playerY)
    # Call enemy function
    enemy(enemyX, enemyY)
    # Update the pygame window
    pygame.display.update()