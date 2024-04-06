import pygame
from physics import Vector
import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, position: Vector, vx: float) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(
            "Images/Player/sprite_image.png").convert_alpha()

        self.position = position
        self.velocity = Vector(vx, 0)
        self.acceleration = Vector(0, 150)

        self.grounded = False

        self.rect = self.image.get_rect(topleft=(position.x, position.y))

    def update(self, dt: float):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.rect.y = self.position.y
        self.rect.x = self.position.x

