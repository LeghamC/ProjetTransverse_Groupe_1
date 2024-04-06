import pygame
from physics import Vector


class Platform(pygame.sprite.Sprite):
    def __init__(self, position: Vector, width: int, height: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))

        self.position = position

        self.rect = self.image.get_rect(topleft=(position.x, position.y))

    def update(self):
        pass
