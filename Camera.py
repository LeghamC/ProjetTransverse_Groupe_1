# -------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - Camera class
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame
import Constants
from Physics import Vector


class Camera:
    def __init__(self, window_size):
        self.position = Vector(0, 0)
        self.window_size = window_size

    def update_position(self, player_rect: pygame.Rect):
        offset_x = player_rect.centerx - self.window_size[0]/2 - self.position.x
        if offset_x > 0:
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

    def render_background(self, bg: pygame.Surface, screen: pygame.Surface):
        x = (-self.position.x * 0.6) % bg.get_width() - bg.get_width()
        screen.blit(bg, (x, 0))
        screen.blit(bg, (x + bg.get_width(), 0))
