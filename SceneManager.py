import pygame
from Scene import *
from button import *


class SceneManager:
    def __init__(self, input_manager):
        self.input_manager = input_manager
        self.current_scene = None
        self.current_scene_index = -1

    def load_scene(self, i):
        if i == self.current_scene_index:
            return
        match i:
            case 0:
                self.current_scene = GameMenu(self.input_manager)
                self.current_scene_index = 0
            case 1:
                self.current_scene = GameScene(0, self.input_manager)
                self.current_scene_index = 1
            case _:
                pass

    def update(self, dt):
        cmd_type, param = self.current_scene.update(dt)
        if cmd_type == EXIT_GAME:
            return 0
        if cmd_type == SWITCH_SCENE:
            self.load_scene(param[0])
            self.current_scene.begin_level()
        return 1
