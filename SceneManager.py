# -------------------------------------------------------------------------------
# Name:        Aux Quatre Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - SceneManager class
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame
from Scene import *
from Button import *

# Object that manages switching between scenes
class SceneManager:
    """handles the creation, updating, and switching of different game scenes."""
    def __init__(self, input_manager):
        self.input_manager = input_manager
        # Reference to the current scene
        self.current_scene = None
        # Index corresponding to that scene
        self.current_scene_index = -1

    def load_scene(self, i):
        """switches between different scenes"""
        if i == MENU_SCENE:
            self.current_scene = GameMenu(self.input_manager)
            self.current_scene_index = MENU_SCENE
        elif i in (WINTER_SCENE, SPRING_SCENE, SUMMER_SCENE, AUTUMN_SCENE):
            self.current_scene = GameScene(i, self.input_manager)
            self.current_scene_index = i

    def update(self, dt):
        """updates the current scene and
        handles scene transitions based on commands returned from the scene update"""
        cmd_type, param = self.current_scene.update(dt)
        if cmd_type == EXIT_GAME:
            return 0
        if cmd_type == SWITCH_SCENE:
            pygame.mixer.music.unload()
            pygame.mixer.music.set_volume(1)
            self.load_scene(param[0])
            self.current_scene.begin_level()
        return 1
