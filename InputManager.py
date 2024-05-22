# -------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - Input Manager class
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame

# Stores Input of different types at each frame
# Used so that any object can access user inputs
class InputManager:
    def __init__(self):
        self.QUIT = 0
        # Three main types of event:
        # 1. Key is pushed on this frame
        # 2. Key is released on this frame
        # 3. Key is being held
        self.KEYDOWN = set()
        self.KEYUP = set()
        self.HELD = set()

    # To be called every frame to update events
    def update(self, events: list[pygame.event.Event]):
        self.KEYDOWN.clear()
        self.KEYUP.clear()
        for event in events:
            match event.type:
                case (pygame.QUIT):
                    self.QUIT = 1
                    break
                case (pygame.KEYDOWN):
                    # print("DOWN: ", event.key)
                    self.KEYDOWN.add(event.key)
                    self.HELD.add(event.key)
                    break
                case (pygame.KEYUP):
                    # print("UP: ", event.key)
                    self.KEYUP.add(event.key)
                    if event.key in self.HELD:
                        self.HELD.remove(event.key)
                    break
