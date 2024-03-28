# -------------------------------------------------------------------------------
# Name:        ???
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project's menu - the game's window
# Created:     01/02/2024
# -------------------------------------------------------------------------------

# IMPORTATIONS OF MODULES
import pygame
from sys import exit
import level_saver
import collisions
import scrolling
import constants

# CONSTANTS
PLAYER_SPEED = 120
FPS = 60

# CREATION OF THE GRAPHIC WINDOW
# Initialization of pygame
pygame.init()
# Opening of pygame window (width ,height)
window = pygame.display.set_mode((1224, 600))
# Name of the game as window's name
pygame.display.set_caption("Shiho<3")
# Control the frame rate
clock = pygame.time.Clock()
font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 30)
active = True

# BACKGROUND_1
# Use of .convert() that helps the game run faster (use .convert_alpha if image seems weird)
# Position pointer for rectangles (topleft,midtop,topright,midleft,center,midright,bottomleft,midbottom,bottomright)
background_1 = pygame.image.load("Images/Backgrounds/background_forest_mountain.png").convert()
background_xpos = 0
background_xpos2 = 612
background_xpos3 = 1224

# DISPLAY OF NUMBER OF RINGS GATHERED
text_score = font.render("Rings  000", True, "Gold")
score_rect = text_score.get_rect(topright = (1215, 10))

# DISPLAY OF TIMER
text_timer = font.render("Timer 00.00", True, "White")
timer_rect = text_timer.get_rect(topright = (1215, 50))

# PLATEFORM SURFACE
plateform = pygame.Surface((50, 50))
plateform_rect = plateform.get_rect(bottomleft = (350, 220))
# Color of the plateform with hex color code
plateform.fill("#BBDE22")

# PLAYER SURFACE
player_shiho = pygame.Surface((50, 50))
player_rect = player_shiho.get_rect(topleft = (5,380))
player_gravity = -20

# GAME OVER SCREEN
#game_over = pygame.image.load("Images/Shiho_calligraphy.png").convert()
game_over_text = font.render("GAME OVER", True, "black")
game_over_rect = game_over_text.get_rect(center = (612,230))

# Loop to keep the window open
while True:
    for event in pygame.event.get():
        # Cross to escape window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.top >= 0:
                # If space key pressed than jump
                player_gravity = -20
        if event.type == pygame.KEYUP:
            # release the key
            print("falling")
    if active:
        # blit = put a surface on a surface
        # The instruction are ordered since the images overlap gradually
        window.blit(background_1,(background_xpos,0))
        window.blit(background_1, (background_xpos2,0))
        window.blit(background_1, (background_xpos3, 0))
        window.blit(text_score, score_rect)
        window.blit(text_timer, timer_rect)
        window.blit(plateform,plateform_rect)

        # Gravity of player's jumps
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 461:
            player_rect.bottom = 460
        window.blit(player_shiho,player_rect)
        # Player moving from left to right
        # print(player_rect.right) can give the coordinate of the right line of the rectangle
        player_rect.right += 1

        #ANIMATION
        # Background moving from right to left
        background_xpos -= 2
        background_xpos2 -= 2
        background_xpos3 -= 2
        if background_xpos == -612 :
            background_xpos = 0
            background_xpos2 = 612
            background_xpos3 = 1224

        # MOUSE FUNCTIONING
        # Display of mouse cursor
        mouse_pos = pygame.mouse.get_pos()

        # COLLISION DETECTION
        if player_rect.colliderect(plateform_rect):
            active = False
        if player_rect.collidepoint(mouse_pos):
            print("Collision cursor")

    else:
        # window.blit(game_over,(612,230))
        window.fill("Red")
        window.blit(game_over_text, game_over_rect)


    pygame.display.update()
    # Rate of 60 images per second so that the game does not run too fast or too slow
    clock.tick(60)
