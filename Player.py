import pygame
from Arrow import ArrowT, ArrowC
from physics import Vector, make_vector_polar
import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, position: Vector, vx: float, input_manager) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.y_factor = 3

        self.input_manager = input_manager

        self.position = position
        self.velocity = Vector(vx, 0)
        self.acceleration = Vector(0, 150)

        self.image = pygame.image.load(
            "Images/Player/sprite_image.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(position.x, position.y))

        self.arrow = ArrowT()
        self.grounded = False


    def update(self, dt: float):
        self.arrow.update(self)
        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt * self.y_factor
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt * self.y_factor
        self.rect.y = self.position.y
        self.rect.x = self.position.x

    def jump(self):
        self.position.y -= 1
        self.velocity.y += make_vector_polar(200, -self.arrow.angle).y
