import pygame


class InputManager:
    def __init__(self):
        self.QUIT = 0
        self.KEYDOWN = set()
        self.KEYUP = set()
        self.HELD = set()

    def update(self, events: list[pygame.event.Event]):
        self.KEYDOWN.clear()
        self.KEYUP.clear()
        for event in events:
            match event.type:
                case (pygame.QUIT):
                    self.QUIT = 1
                    break
                case (pygame.KEYDOWN):
                    self.KEYDOWN.add(event.key)
                    self.HELD.add(event.key)
                    break
                case (pygame.KEYUP):
                    self.KEYUP.add(event.key)
                    if event.key in self.HELD:
                        self.HELD.remove(event.key)
                    break
