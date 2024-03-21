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
from physics import *
from button import *

# Initialization of pygame
pygame.init()

# Create a window for the menu
window = pygame.display.set_mode((600, 500)) # width, height
pygame.display.set_caption("Shiho<3")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/future-timesplitters/Future TimeSplitters.otf", 30)
menu = True
active = True

def draw_menu():
    menu_button = Button("Parameters",300,250,100,40,active) # Border of the button
    menu_button.draw()
    return menu_button.click()

def draw_game():
    button = Button("Play",10,5,1,2,active)
    button.draw()
    return button.click()

while active:
    window.fill("black")

    if menu:
        draw_menu()
    else:
        menu = draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    pygame.display.update()
    clock.tick(60)