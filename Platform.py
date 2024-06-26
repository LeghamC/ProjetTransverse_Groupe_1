# -------------------------------------------------------------------------------
# Name:        Aux Quatre Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - Plateform class
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame
from Physics import Vector

class Platform(pygame.sprite.Sprite):
    SURFACES = {}

    def __init__(self, position: Vector, width: int, height: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        if width not in Platform.SURFACES:
            Platform.SURFACES[width] = pygame.Surface((width, height))
        self.image = Platform.SURFACES[width]

        self.position = position

        self.rect = self.image.get_rect(topleft=(position.x, position.y))

        self.tangible = True

    def update(self):
        pass
