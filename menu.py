# -------------------------------------------------------------------------------
# Name:        ???
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project's menu - the game's window
# Created:     01/02/2024
# -------------------------------------------------------------------------------

# IMPORTATIONS OF MODULES
import pygame
import math
from sys import exit
from physics import *

# Initialization of pygame
pygame.init()

# Create a window for the menu
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Shiho<3")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/future-timesplitters/Future TimeSplitters.otf", 30)
active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)