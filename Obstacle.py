# -------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - obstacle class that create the rectangles on which
#              the player must jump
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame
from Physics import Vector


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position: Vector, width: int, height: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.position = position
        self.rect = self.image.get_rect(topleft=(position.x, position.y))

    def update(self):
        pass
