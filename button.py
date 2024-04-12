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
font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 30)

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
    """
    def __init__(self, text: str, x_pos: int, y_pos: int, width: int, height: int, image: str = "") -> None:
        self.text = text
        self.image = pygame.image.load("Images/settings.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.button_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def draw(self):
        """
                Make the characteristics of the button (color, surface) and print it on the screen
        """
        if self.click():
            pygame.draw.rect(window, "dark blue", self.button_rect, 0, 5) # Color when collision with the button
        else:
            pygame.draw.rect(window, "black", self.button_rect) # color of the button's inside
        pygame.draw.rect(window, "dark blue", self.button_rect, 4, 5) # Border of the button
        if self.text != "":
            button_text = font.render(self.text, True, "white")
            window.blit(button_text, (self.x_pos + 3, self.y_pos + 3))
        else:
            window.blit(self.image,(self.x_pos + 3, self.y_pos + 3))

    def click(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
