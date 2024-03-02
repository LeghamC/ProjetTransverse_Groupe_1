import pygame
import constants


def update_camera_pos(camera_x: int, player_rect: pygame.Rect) -> int:
    player_offset = player_rect.centerx - constants.SCREEN_W/2 - camera_x
    if (player_offset > 0):
        camera_x += player_offset
    return camera_x


def camera_render(
        surface: pygame.Surface,
        rect: pygame.Rect,
        screen: pygame.Surface,
        camera_x: int,
        z_index: int = 1) -> None:
    screen.blit(surface, (rect.x - (camera_x * z_index), rect.y))
