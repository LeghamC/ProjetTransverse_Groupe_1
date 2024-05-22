# -------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - Player class
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame
from Arrow import ArrowT, ArrowC
from Physics import Vector, make_vector_polar
import Constants


class Player(pygame.sprite.Sprite):
    def __init__(self, position: Vector, vx: float, input_manager) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.jump_force = 300
        self.y_factor = 3

        self.input_manager = input_manager

        self.position = position
        self.velocity = Vector(vx, 0)
        self.acceleration = Vector(0, 150)

        self.arrow = ArrowT()  # represent the aiming direction
        self.grounded = False  # True if player on the ground

    def set_image(self, filename):
        self.image = pygame.transform.scale(
            pygame.image.load(filename).convert_alpha(),
            (40, 40)
        )
        self.rect = self.image.get_rect(topleft=(self.position.x, self.position.y))

    def update(self, dt: float):
        self.arrow.update(self)
        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt * self.y_factor
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt * self.y_factor
        self.rect.y = self.position.y
        self.rect.x = self.position.x

    def jump(self):
        """Adjusts the player's position slightly upward to not have intersection with a platform.
        Creates a vector representing the jump force in direction opposite to arrow's angle.
        Updates the player's vertical velocity based on the jump force."""
        self.position.y -= 1
        self.velocity.y += make_vector_polar(self.jump_force, -self.arrow.angle).y