# -------------------------------------------------------------------------------
# Name:        ???
# Author:      Lélia
# Purpose:     Project's menu - the menu's window
# Created:     01/02/2024
# -------------------------------------------------------------------------------

# IMPORTATION OF MODULES
import pygame
import math
from sys import exit
from button import *

# Initialization of pygame
pygame.init()

# Create a window for the menu
window = pygame.display.set_mode((600, 500))  # width, height
pygame.display.set_caption("Shiho<3")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 20)
background_menu = pygame.image.load("Images/Backgrounds/minou_in_the_street_playboy.jpeg").convert_alpha()
background_menu = pygame.transform.scale(background_menu, (600, 500))
shiho = pygame.image.load("Images/Player/Shiho_calligraphy.png").convert_alpha()
shiho = pygame.transform.scale(shiho, (40, 20))
main_menu = False
menu_command = 0
active = True

# Create the buttons outside the draw_menu() function
exit_butt = Button('Exit', 10, 10, 50, 25)
settings_butt = Button('Spring', 120, 180, 100, 50)
level1_butt = Button('Spring', 120, 180, 100, 50)
level2_butt = Button('Summer', 120, 240, 100, 50)
level3_butt = Button('Fall', 120, 300, 100, 50)
level4_butt = Button('Winter', 120, 360, 100, 50)

def draw_menu():
    command = -1
    window.blit(background_menu, (0, 0))  # Draw background image first
    pygame.draw.rect(window, 'brown', [120, 120, 260, 40], 0, 5)
    pygame.draw.rect(window, 'dark blue', [120, 120, 260, 40], 5, 5)
    menu_title = font.render('Shiho <3', True, 'green')
    window.blit(menu_title, (135, 127))

    # Draw all buttons
    exit_butt.draw()
    settings_butt.draw()
    level1_butt.draw()
    level2_butt.draw()
    level3_butt.draw()
    level4_butt.draw()

    # Check for clicks on buttons
    if exit_butt.click():
        command = 0
    if level1_butt.click():
        command = 1
    if level2_butt.click():
        command = 2
    if level3_butt.click():
        command = 3
    if level4_butt.click():
        command = 4

    return command

def draw_game():
    window.blit(background_menu, (0, 0))
    menu_butt = Button("Game menu (Shiho <3)", 130, 10, 320, 70)
    menu_butt.draw()
    menu = menu_butt.click()
    return menu

while active:
    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command > 0:
            text_transition = font.render(f'Button: {menu_command}', True, "white")
            window.blit(text_transition, (300, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()

