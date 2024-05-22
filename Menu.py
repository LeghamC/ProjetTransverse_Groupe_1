# -------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project's menu - the gameplay window
# Created:     01/02/2024
# -------------------------------------------------------------------------------

# IMPORTATION OF MODULES
import pygame
import math
from sys import exit
from Button import *
from SceneManager import *
from Scene import *
from InputManager import *
from Constants import *

FPS = 60

# Initialization of pygame
pygame.init()

# Create a window for the menu
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))  # width, height
pygame.display.set_caption("Aux Quatre Temps")
clock = pygame.time.Clock()
dt = 0
font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 20)
Button.font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 30)

# Initialize the Input Manager
# (Stores user input)
input_manager = InputManager()

# Initializes the Scene Manager
# (Stores the current scene and allows to change scenes)
scene_manager = SceneManager(input_manager)
scene_manager.load_scene(0)

active = True

# Main Game Loop
while active:
    input_manager.update(pygame.event.get())
    if input_manager.QUIT:
        pygame.quit()
        exit()
    active = active and scene_manager.update(dt)
    scene_manager.current_scene.draw(window)

    pygame.display.update()
    # dt in seconds
    dt = clock.tick(FPS) * 0.001

pygame.quit()
exit()
