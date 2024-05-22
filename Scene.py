# -------------------------------------------------------------------------------
# Name:        Aux Quatre Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project - Scene class
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame.mixer_music

from Button import *
from Constants import *
from Player import *
from Camera import *
from Collisions import *
from InputManager import *
import Level_saver

# CONSTANTS
MENU_SCENE = 0
WINTER_SCENE = 1
SPRING_SCENE = 2
SUMMER_SCENE = 3
AUTUMN_SCENE = 4

PLAYING = 0
PAUSED = 1
GAME_OVER = 2
END_SCREEN = 3

pygame.font.init()


# Class to Inherit to create a Scene
class Scene:
    # Create the game scenes
    def __init__(self, input_manager: InputManager):
        self.window: pygame.Surface
        self.background: pygame.Surface
        self.objects: list
        self.states: list
        self.current_state: int

        self.input_manager = input_manager

    # Methods to overwrite
    def update(self, dt=0):
        pass

    def begin_level(self):
        return

    def get_active_objects(self):
        if self.current_state == -1:
            return
        for i in self.states[self.current_state]:
            yield self.objects[i]
        return

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.window, (SCREEN_W, SCREEN_H)), (0, 0))


class GameMenu(Scene):
    # Main menu of the game
    def __init__(self, input_manager):
        super().__init__(input_manager)
        self.window = pygame.Surface((SCREEN_W, SCREEN_H))
        self.background = pygame.transform.scale(
            pygame.image.load("Images/Menu/MenuAmsterdamOneUpdate.png").convert_alpha(),
            (SCREEN_W, SCREEN_H)
        )
        # All the buttons appearing in the scene
        self.objects = [
            button_by_center('Play', SCREEN_W//2, SCREEN_H - 60, 85, 50,
                             cmd=(SWITCH_STATE, [1])),
            Button('Exit', 20, 12, 80, 50,
                   cmd=(EXIT_GAME, [])),
            Button('', SCREEN_W-65, 12, 45, 45,
                   image="Images/SettingsIcon.png", cmd=(SWITCH_STATE, [2])),
            button_by_center('Winter', 0.13*SCREEN_W, SCREEN_H-60, 110, 50,
                             cmd=(SWITCH_SCENE, [WINTER_SCENE])),
            button_by_center('Summer', 0.39*SCREEN_W, SCREEN_H-60, 130, 50,
                             cmd=(SWITCH_SCENE, [SUMMER_SCENE])),
            button_by_center('Spring', 0.65*SCREEN_W, SCREEN_H-60, 110, 50,
                             cmd=(SWITCH_SCENE, [SPRING_SCENE])),
            button_by_center('Fall', .91*SCREEN_W, SCREEN_H-60, 80, 50,
                             cmd=(SWITCH_SCENE, [AUTUMN_SCENE])),
        ]

        # Gives which button should be visible according to a certain state
        self.states = [
            [0],
            [1, 2, 3, 4, 5, 6],
            [0]
        ]

        pygame.mixer.music.load("Musics/adaggio.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        self.current_state = 0

    def update(self, dt=0):
        cmd_type, param = DO_NOTHING, []
        self.window.blit(self.background, (0, 0))
        for button in self.get_active_objects():
            button.draw(self.window)
            if button.is_clicked():
                cmd_type, param = button.cmd
                break

        if cmd_type == SWITCH_STATE:
            self.current_state = param[0]
        elif cmd_type == SWITCH_SCENE:
            return SWITCH_SCENE, param
        elif cmd_type == EXIT_GAME:
            return EXIT_GAME, []
        return DO_NOTHING, []

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.window, (SCREEN_W, SCREEN_H)), (0, 0))


class GameScene(Scene):
    # Main gameplay scenes
    def __init__(self, i, input_manager):
        super().__init__(input_manager)
        self.PLAYER_SPEED = 200

        self.window = pygame.Surface((SCREEN_W, SCREEN_H))
        self.current_state = PLAYING

        self.player = Player(Vector(0, 200), self.PLAYER_SPEED, self.input_manager)
        self.camera = Camera((SCREEN_W, SCREEN_H))

        self.font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 30)
        self.pause_text = self.font.render("PAUSED", True, "white")
        self.pause_rect = self.pause_text.get_rect(center=(SCREEN_W//2, SCREEN_H//3))
        self.game_over_text = self.font.render("GAME OVER", True, "black")
        self.game_over_rect = self.game_over_text.get_rect(center=(SCREEN_W//2, SCREEN_H//3))

        self.background_x = 0

        self.active = False

        self.scene_id = i

        # Loads the level according to which scene
        # has to be loaded
        if i == WINTER_SCENE:
            self.background = pygame.image.load("Images/Backgrounds/WinterBG.jpg").convert_alpha()
            self.background_x_max = self.background.get_size()[0]
            self.objects = Level_saver.list_of_elements(
                Level_saver.load_level("levels/Winter/content.csv"),
                self.PLAYER_SPEED
            )
            pygame.mixer.music.load("Musics/winter.ogg")
            self.player.set_image("Images/Player/WinterCharacter.png")
        elif i == SPRING_SCENE:
            self.background = pygame.image.load("Images/Backgrounds/SpringBG.jpg").convert_alpha()
            self.background_x_max = self.background.get_size()[0]
            self.objects = Level_saver.list_of_elements(
                Level_saver.load_level("levels/Spring/content.csv"),
                self.PLAYER_SPEED
            )
            pygame.mixer.music.load("Musics/spring.ogg")
            self.player.set_image("Images/Player/SpringCharacter.png")

        self.restart_btn = button_by_center("Restart", SCREEN_W//4, SCREEN_H-60,
                                            115, 50, cmd=(SWITCH_SCENE, [self.scene_id]))
        self.menu_btn = button_by_center("Main Menu", 3*SCREEN_W//4, SCREEN_H-60,
                                         175, 50, cmd=(SWITCH_SCENE, [0]))

    def begin_level(self):
        self.active = 1
        pygame.mixer.music.play()

    def update(self, dt=0):
        if not self.active:
            return DO_NOTHING, []
        if pygame.K_p in self.input_manager.KEYDOWN:
            if self.current_state == 0:
                self.current_state = 1
                pygame.mixer.music.pause()
            else:
                self.current_state = 0
                pygame.mixer.music.unpause()

        if self.current_state == PLAYING:
            return self.update_playing(dt)
        elif self.current_state == PAUSED:
            if self.menu_btn.is_clicked():
                return self.menu_btn.cmd
            elif self.restart_btn.is_clicked():
                return self.restart_btn.cmd
            return DO_NOTHING, []
        elif self.current_state == GAME_OVER:
            if self.menu_btn.is_clicked():
                return self.menu_btn.cmd
            elif self.restart_btn.is_clicked():
                return self.restart_btn.cmd
            return DO_NOTHING, []
        elif self.current_state == END_SCREEN:
            return DO_NOTHING, []

    def update_playing(self, dt):
        # self.background_x = (self.background_x - 2) % self.background_x_max - self.background_x_max

        self.player.update(dt)
        if self.player.rect.bottom >= SCREEN_H:
            self.player.velocity.y = 0
            self.player.position.y = SCREEN_H - self.player.rect.height
            self.player.rect.bottom = SCREEN_H
        # print("Player grounded: ", self.player.grounded)
        # print("Aiming: ", self.player.arrow.aiming)

        self.camera.update_position(self.player.rect)

        removed = 0
        for element in self.objects:
            if element.rect.right - self.camera.position.x < 0:
                removed += 1
            elif element.rect.right < self.player.rect.left:
                element.tangible = False
            elif element.rect.x > self.player.rect.right:
                break
            if element.tangible and self.player.rect.colliderect(element.rect.move(0, -1)):
                if top_collision(self.player.rect, element.rect.move(0, -1)):
                    self.player.position.y = element.rect.top - self.player.rect.height
                    self.player.rect.bottom = element.rect.top
                    self.player.velocity.x = self.PLAYER_SPEED
                    self.player.velocity.y = 0
                else:
                    self.current_state = GAME_OVER
                    pygame.mixer.music.stop()
        self.objects = self.objects[removed:]
        self.player.grounded = (self.player.velocity.y == 0)

        return DO_NOTHING, []

    def draw(self, screen):
        if not self.active:
            return

        if self.current_state == PLAYING:
            self.draw_playing()
        elif self.current_state == PAUSED:
            self.draw_playing()
            s = pygame.Surface((SCREEN_W, SCREEN_H))
            s.set_alpha(200)
            self.window.blit(s, (0, 0))
            self.window.blit(self.pause_text, self.pause_rect)
            self.restart_btn.draw(self.window)
            self.menu_btn.draw(self.window)
        elif self.current_state == GAME_OVER:
            self.window.fill("red")
            self.window.blit(self.game_over_text, self.game_over_rect)
            self.restart_btn.draw(self.window)
            self.menu_btn.draw(self.window)

        screen.blit(pygame.transform.scale(self.window, screen.get_size()), (0, 0))

    def draw_playing(self):
        # self.window.blit(self.background, (self.background_x, 0))
        # self.window.blit(self.background, (self.background_x + self.background_x_max, 0))
        # self.window.blit(self.background, (self.background_x+2*self.background_x_max, 0))

        self.camera.render_background(self.background, self.window)

        for element in self.objects:
            if element.rect.x - self.camera.position.x > SCREEN_W:
                break
            self.camera.render_element(
                pygame.Surface((element.rect.w, element.rect.h)),
                element.rect,
                self.window
            )

        if self.player.arrow.aiming:
            # Draw the arrow
            self.camera.render_element(
                self.player.arrow.rotated_image,
                self.player.arrow.rect,
                self.window
            )

        self.camera.render_element(
            self.player.image,
            self.player.rect,
            self.window
        )
