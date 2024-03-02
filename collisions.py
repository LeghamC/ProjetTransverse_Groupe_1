import pygame


# Checks if there is a collision from the top
# (= rect1 on top of rect2)
def top_collision(rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
    return (rect1.bottom > rect2.top) and (rect1.top < rect2.top)
