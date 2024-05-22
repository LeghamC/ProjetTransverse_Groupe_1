# ----------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - create, save, load, and convert level content for the game
# Created:     01/02/2024
# ----------------------------------------------------------------------------------
import csv
import pygame
from Physics import Vector
from Platform import Platform
from Constants import *


# Used to signify if the note is a rest or an actual note
# When manually creating level content.
REST = False
AUDIBLE = True


# Allows to write level content onto a new/pre-existing file
def save_level(file_name: str, file_content: list[list]) -> None:
    """Saves the level content in a CSV file which includes headers and rows of data,
    each represent an element of the level (platform or note or more in the future)."""
    with open(file_name, 'w', newline="") as csv_file:
        writer = csv.writer(
            csv_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC
        )
        writer.writerow(["time", "duration", "height", "type"])
        for element in file_content:
            writer.writerow(element)
    print(f"\nContent Successfully Saved in {file_name}")


# Allows to load the content of a level from the name of the file
# Returns the content of the level
def load_level(file_name: str) -> list[list]:
    """Loads level content from a CSV file and returns it as a list of lists.
Skips the header row to ensure only the data rows are processed."""
    content = []
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(
            csv_file,
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC
        )
        for row in reader:
            if not isinstance(row[0], str):
                content.append(row)
    return content


def position_on_screen(element_time: float, player_speed: int) -> int:
    """Compute the x-coordinate position on the screen based on the element's time and the player's speed."""
    return int(player_speed * element_time)

def width_element(element_duration: float, player_speed: int) -> float:
    """Takes an element's duration and the player's speed and returns the width
that the element should have"""
    return element_duration * player_speed


def list_of_elements(level_content: list[list],
                     player_speed: int) -> list[pygame.sprite.Sprite]:
    """Converts level content into a list Sprite objects (Platforms).
    Uses the position_on_screen and width_element functions to compute the position and dimensions of each element."""
    elements = []
    for i in level_content:
        x = position_on_screen(i[0], player_speed)
        y = i[2]
        h = 20
        w = width_element(i[1], player_speed)

        elements.append(Platform(Vector(x, y), w, h))
    return elements


def height_level_to_height(height_level: int) -> int:
    """Converts a simplified height level into a pixel value to position elements vertically on the screen."""
    return SCREEN_H*(1 - height_level * 5 / 46)

def make_content(tempo: int, notes: list[list[int | bool]]):
    """Allows to create level_content manually note: [float note_length, int height_level, bool REST/AUDIBLE]"""
    elements = []
    current_time = 0.0
    time_multiplier = 60 / tempo
    for note in notes:
        duration = note[0] * time_multiplier
        if note[2] == AUDIBLE:
            height = height_level_to_height(note[1])
            elements.append([current_time, duration, height, 0])
        current_time += duration
    return elements


# Winter Level Content
"""
winter_content = make_content(
    tempo=150,
    notes=[
        [21, 0, REST],
        [4, 3, AUDIBLE],  # 1

        [2, 4, AUDIBLE],
        [2, 3, AUDIBLE],
        [4, 2, AUDIBLE],  # 2

        [2, 3, AUDIBLE],
        [2, 2, AUDIBLE],
        [4, 1, AUDIBLE],  # 3

        [2, 2, AUDIBLE],
        [2, 1, AUDIBLE],
        [4, 0, AUDIBLE],  # 4

        [2, 1, AUDIBLE],
        [2, 0, AUDIBLE],

        [2, 3, AUDIBLE],
        [2, 4, AUDIBLE],
        [2, 5, AUDIBLE],
        [2, 6, AUDIBLE],
        [2, 8, AUDIBLE],

        [2, 7, AUDIBLE],
        [2, 6, AUDIBLE],
        [2, 5, AUDIBLE],
        [2, 6, AUDIBLE],
        [2, 7, AUDIBLE],
        [2, 8, AUDIBLE],
        [2, 7, REST],

        [2, 6, AUDIBLE],
        [2, 5, AUDIBLE],
        [2, 4, AUDIBLE],
        [2, 6, AUDIBLE],
        [2, 7, AUDIBLE],
        [2, 8, AUDIBLE],
        [2, 7, REST],

        [2, 6, AUDIBLE],
        [2, 5, AUDIBLE],
        [2, 4, AUDIBLE],
        [2, 5, AUDIBLE],
        [2, 6, AUDIBLE],
        [2, 5, AUDIBLE],
        [2, 6, AUDIBLE],
        [2, 5, AUDIBLE],
        [2, 6, AUDIBLE],
        [2, 7, AUDIBLE],
        [2, 6, AUDIBLE],

        [4, 5, AUDIBLE],
        [4, 3, AUDIBLE],

        [4, 6, AUDIBLE],
        [4, 4, AUDIBLE],

        [4, 7, AUDIBLE],
        [4, 5, AUDIBLE],

        [1, 1, REST],
        [4, 4, AUDIBLE],
        [4, 3, AUDIBLE],

        [4, 6, AUDIBLE],
        [3, 5, AUDIBLE],
    ]
)
"""

spring_content = make_content(
    tempo=100,
    notes=[
        [6, 1, REST],
        [4, 2, AUDIBLE],
        [4, 1, REST],
        [2, 2, AUDIBLE],
        [2, 1, AUDIBLE],
        [2, 1, REST],
        [2, 1, AUDIBLE],
        [2, 2, AUDIBLE],
        [2, 3, AUDIBLE],
        [2, 4, AUDIBLE],
        [2, 3, AUDIBLE],
        [2, 2, AUDIBLE],
        [2, 1, AUDIBLE],
        [2, 2, AUDIBLE],
        [2, 3, AUDIBLE],
        [2, 4, AUDIBLE],
        [2, 3, AUDIBLE],
        [2, 4, AUDIBLE],

        [2, 2, AUDIBLE],
        [2, 1, AUDIBLE],
        [2, 3, AUDIBLE],
        [2, 2, AUDIBLE],
        [2, 3, AUDIBLE],
        [2, 4, AUDIBLE],
        [2, 3, AUDIBLE],

        [1, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [0.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [1, 1, AUDIBLE],

        [1, 2, AUDIBLE],

        [1.5, 1, AUDIBLE],
        [0.5, 1, REST],
        [1.5, 1, AUDIBLE],
        [0.5, 1, REST],

        [2, 3, AUDIBLE],

        [2, 5, AUDIBLE],

        [2, 5, AUDIBLE],
        [2, 4, AUDIBLE],
        [2, 3, AUDIBLE],

        [1, 4, AUDIBLE],

        [2, 3, AUDIBLE],
        [2, 5, AUDIBLE],
    ]
)

if __name__ == "__main__":
    # save_level("levels/Winter/content.csv", winter_content)
    # save_level("levels/Summer/content.csv", summer_content)
    # save_level("levels/Autumn/content.csv", autumn_content)
    save_level("levels/Spring/content.csv", spring_content)
