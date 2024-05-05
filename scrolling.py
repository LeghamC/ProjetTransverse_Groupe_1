import pygame
import constants
from physics import Vector


class Camera:
    def __init__(self, window_size):
        self.position = Vector(0, 0)
        self.window_size = window_size

    def update_position(self, player_rect: pygame.Rect):
        offset_x = player_rect.centerx - self.window_size[0]/2 - self.position.x
        if (offset_x > 0):
            self.position.x += offset_x

    # Takes a surface and its position, with a screen and draws the elements
    # on the screen.
    # (The z_index controls how much the camera position
    #  impacts the given element's position)
    def render_element(
            self,
            surface: pygame.Surface,
            rect: pygame.Rect,
            screen: pygame.Surface,
            z_index: int = 1) -> None:
        screen.blit(surface, (rect.x - (self.position.x * z_index), rect.y))
