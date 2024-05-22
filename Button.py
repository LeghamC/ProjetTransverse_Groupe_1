# -------------------------------------------------------------------------------
# Name:        Aux Quatre Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - Button class
# Created:     18/03/2024
# -------------------------------------------------------------------------------

# IMPORTATION OF MODULES
import pygame

DO_NOTHING = 0
MODIFY_PARAMETER = 1
SWITCH_SCENE = 2
SWITCH_STATE = 3
EXIT_GAME = 4


# BUTTON CLASS TO CLICK
class Button:
    font = None
    """
        Make buttons on which you can click.

        Args:
            text (str): Name of button.
            x_pos (int): position on x-axis of the button
            y_pos (int): position on y-axis of the button
            width (int): width of the button
            height (int): height of the button
    """
    def __init__(
            self, text: str, x_pos: int, y_pos: int, width: int, height: int,
            image: str = "", cmd=(DO_NOTHING, [])) -> None:
        self.text = text
        self.image = pygame.image.load("Images/SettingsIcon.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40)).convert_alpha()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.button_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        self.cmd = cmd

    def draw(self, surface):
        """
                Make the characteristics of the button (color, surface) and print it on the screen.
        """
        if self.is_clicked():
            pygame.draw.rect(surface, "white", self.button_rect, 0, 5) # Color when collision with the button
        else:
            pygame.draw.rect(surface, 'black', self.button_rect) # color of the button's inside
        pygame.draw.rect(surface, "white", self.button_rect, 4, 5) # Border of the button
        if self.text != "":
            button_text = Button.font.render(self.text, True, "white")
            surface.blit(button_text, (self.x_pos + 3, self.y_pos + 3))
        else:
            surface.blit(self.image, (self.x_pos + 3, self.y_pos + 3))

    def is_clicked(self):
        return self.button_rect.collidepoint(pygame.mouse.get_pos()) and \
               pygame.mouse.get_pressed()[0]

def button_by_center(text, x, y, w, h, img="", cmd=(DO_NOTHING, [])):
    """allow to specify the center position, rather than the top-left corner when called"""
    x = x - w//2
    y = y - h//2
    return Button(text, x, y, w, h, img, cmd)
