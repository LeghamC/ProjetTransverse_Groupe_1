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
import gameplay

# Initialization of pygame
pygame.init()

# Create a window for the menu
window = pygame.display.set_mode((600, 500))  # width, height
pygame.display.set_caption("Aux Quatres Temps")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 20)
Button.font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 30)
background_menu = pygame.image.load("Images/Menu/MenuAmsterdamOne.png").convert_alpha()
background_menu = pygame.transform.scale(background_menu, (600, 500))
shiho = pygame.image.load("Images/Player/WinterCharacter.png").convert_alpha()
shiho = pygame.transform.scale(shiho, (40, 20))
main_menu = False
menu_command = -1
active = True

# Create all the buttons
exit_butt = Button('Exit', 20, 12, 80, 50,
                   cmd=(EXIT_GAME, []))
settings_butt = Button('', 535, 12, 45, 45,
                       image="Images/SettingsIcon.png", cmd=(SWITCH_STATE, 2))
level1_butt = Button('Winter', 20, 400, 110, 50)
level2_butt = Button('Summer', 175, 400, 130, 50)
level3_butt = Button('Spring', 335, 400, 110, 50)
level4_butt = Button('Fall', 495, 400, 80, 50)

def draw_menu():
    command = -1
    window.blit(background_menu, (0, 0))  # Draw background image first
    # pygame.draw.rect(window, 'black', [175, 100, 260, 40], 0, 5)
    # pygame.draw.rect(window, 'dark blue', [175, 100, 260, 40], 5, 5)
    # menu_title = font.render('Aux Quatre Temps', True, 'white')
    # window.blit(menu_title, (260, 105))

    # Draw all the buttons
    exit_butt.draw(window)
    settings_butt.draw(window)
    level1_butt.draw(window)
    level2_butt.draw(window)
    level3_butt.draw(window)
    level4_butt.draw(window)

    # Check for clicks on buttons
    if exit_butt.is_clicked():
        command = 0
    if level1_butt.is_clicked():
        command = 1
    if level2_butt.is_clicked():
        command = 2
    if level3_butt.is_clicked():
        command = 3
    if level4_butt.is_clicked():
        command = 4
    if settings_butt.is_clicked():
        command = 5

    return command


def draw_game():
    window.blit(background_menu, (0, 0))
    menu_butt = Button("Play", 250, 440, 85, 50)
    menu_butt.draw(window)
    menu = menu_butt.is_clicked()
    return menu


while active:
    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command > -1 and menu_command!= 0 and menu_command != 1:
            text_transition = font.render(f'incoming: {menu_command}', True, "white")
            window.blit(text_transition, (200, 100))
        elif menu_command == 0:
            active = False
        elif menu_command == 1:
            gameplay.GAME()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()

