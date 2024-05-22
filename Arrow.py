# -------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project Arrow file - 2 types of arrow class
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame
from Physics import Vector
import math
import Constants


class Arrow:
    def __init__(self) -> None:
        self.image = pygame.transform.scale(
            pygame.image.load("Images/arrow_beta.png").convert_alpha(),
            (40, 20)
        )
        self.rotated_image = self.image
        self.rect = self.rotated_image.get_rect(center=(0, 0))

        self.position = Vector()
        self.angle = 0
        self.radius = 50

        self.aiming = False

    def update(self, player):
        pass

    def reinitialize(self):
        pass


class ArrowT(Arrow):
    """type of arrow that Automatically oscillates the aiming angle
    and triggers a jump when the space key is released."""
    def __init__(self) -> None:
        super().__init__()
        self.direction = 1

    def update(self, player):
        if pygame.K_SPACE in player.input_manager.KEYUP:
            player.jump()
            self.reinitialize()
        self.aiming = player.grounded and pygame.K_SPACE in player.input_manager.HELD
        if not self.aiming:
            return
        self.position.x = player.rect.centerx + self.radius * math.cos(math.radians(self.angle))
        self.position.y = player.rect.centery - self.radius * math.sin(math.radians(self.angle))

        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotated_image.get_rect(center=(self.position.x, self.position.y))

        # Increment arrow angle for next frame
        self.angle += 5 * self.direction

        # Change direction at 90 and -90 degrees
        if self.angle > 90 or self.angle < 0:
            self.direction *= -1

    def reinitialize(self):
        self.angle = 0
        self.direction = 1
        self.aiming = False


class ArrowC(Arrow):
    """type of arrow that allows the player to manually control the aiming angle
    with specific keys and triggers a jump when the space key is pressed."""
    def __init__(self) -> None:
        super().__init__()

    def update(self, player):
        self.aiming = player.grounded
        if not self.aiming:
            return
        self.position.x = player.rect.centerx + self.radius * math.cos(math.radians(self.angle))
        self.position.y = player.rect.centery - self.radius * math.sin(math.radians(self.angle))

        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotated_image.get_rect(center=(self.position.x, self.position.y))

        # Increment arrow angle for next frame
        if pygame.K_z in player.input_manager.HELD:
            self.angle += 5
        if pygame.K_s in player.input_manager.HELD:
            self.angle -= 5
        if pygame.K_SPACE in player.input_manager.KEYDOWN:
            player.jump()
            self.reinitialize()

        # Change direction at 90 and -90 degrees
        if self.angle > 90:
            self.angle = 90
        elif self.angle < -90:
            self.angle = -90

    def reinitialize(self):
        print("Arrow Reset")
        self.angle = 0
        self.aiming = False