# -------------------------------------------------------------------------------
# Name:        ???
# Author:      Lélia
# Purpose:     Button to click
# Created:     18/03/2024
# -------------------------------------------------------------------------------

# IMPORTATION OF MODULES
import pygame
pygame.init()

window = pygame.display.set_mode((600, 500)) # width, height
font = pygame.font.Font("Font/future-timesplitters/Future TimeSplitters.otf", 30)

# BUTTON CLASS TO CLICK
class Button :
    """
        Make buttons on which you can click.

        Args:
            text (str): Name of button.
            x_pos (int): position on x-axis of the button
            y_pos (int): position on y-axis of the button
            width (int): width of the button
            height (int): height of the button
            active (bool): test of if the button is clickable
    """
    def __init__(self, text: str, x_pos: int, y_pos: int, width: int, height: int, active: bool) -> None:
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.active = active
        self.draw() # make the button directly when called

    def draw(self):
        """
                Make the characteristics of the button (color, surface) and print it on the screen
        """
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        if self.active:
            if self.click():
                pygame.draw.rect(window, "dark grey", button_rect, 0, 5) # Color when collision with the button
            else:
                pygame.draw.rect(window, "black", button_rect, 0, 5) #color of inside the button
        pygame.draw.rect(window, "white", button_rect, 2, 5) # Border of the button
        button_text = font.render(self.text, True, "white")
        window.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    def click(self):
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if button_rect.collidepoint(mouse_pos) and self.active and left_click:
            return True
        else:
            return False
