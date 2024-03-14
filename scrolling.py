import pygame
import constants


# Updates the camera x position according to the player's position
# (Returns the new position)
def update_camera_pos(camera_x: int, player_rect: pygame.Rect) -> int:
    player_offset = player_rect.centerx - constants.SCREEN_W/2 - camera_x
    if (player_offset > 0):
        camera_x += player_offset
    return camera_x


# Takes a surface and its position, with a screen and the camera position
# and draws the elements on the screen accordingly
# (The z_index controls how much the camera position
#  impacts the given element's position)
def camera_render(
        surface: pygame.Surface,
        rect: pygame.Rect,
        screen: pygame.Surface,
        camera_x: int,
        z_index: int = 1) -> None:
    screen.blit(surface, (rect.x - (camera_x * z_index), rect.y))
