import csv
import pygame


# Used to signify if the note is a rest or an actual note
# When manually creating level content.
REST = False
AUDIBLE = True


# Allows to write level content onto a new/pre-existing file
def save_level(file_name: str, file_content: list[list]) -> None:
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
def load_level(file_name: str) -> list[list]:
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
    return int(player_speed * element_time)


def length_element(element_duration: float, player_speed: int) -> int:
    return element_duration * player_speed


# Takes the content of a level and returns a list of rectangles
# associated with this content
def list_of_elements(level_content: list[list],
                     player_speed: int) -> list[pygame.Rect]:
    elements = []
    for i in level_content:
        x = position_on_screen(i[0], player_speed)
        y = i[2]
        h = 20
        w = length_element(i[1], player_speed)

        elements.append(pygame.Rect(x, y, w, h))
    return elements


# Allows to represent the height of an element as a small integer
# Example: height_level: 1 -> height: 410
def height_level_to_height(height_level: int) -> int:
    return 460 - height_level * 50


# Allows to create level_content manually
# note: [float note_length, int height_level, bool REST/AUDIBLE]
def make_content(tempo: int, notes: list[list[float, int, bool]]):
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


level_content = make_content(
    tempo=80,
    notes=[
        [1, 0, REST],
        [4, 0, REST],

        [1, 2, AUDIBLE],
        [1, 3, AUDIBLE],
        [2, 5, AUDIBLE],

        [1, 5, AUDIBLE],
        [1, 4, AUDIBLE],
        [2, 3, AUDIBLE],

        [1, 4, AUDIBLE],
        [1, 4, AUDIBLE],
        [1, 3, AUDIBLE],
        [1, 4, AUDIBLE],

        [4, 2, AUDIBLE]
    ]
)

if __name__ == "__main__":
    print(level_content)
    save_level("levels/level_0/content.csv", level_content)
