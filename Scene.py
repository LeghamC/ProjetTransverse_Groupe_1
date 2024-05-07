import pygame.mixer_music

from button import *
from constants import *
from Player import *
from scrolling import *
from collisions import *
from InputManager import *
import level_saver

class Scene:
    def __init__(self, input_manager: InputManager):
        self.window: pygame.Surface
        self.background: pygame.Surface
        self.objects: list
        self.states: list
        self.current_state: int

        self.input_manager = input_manager

    def update(self, dt=0):
        pass

    def get_active_objects(self):
        if self.current_state == -1:
            return
        for i in self.states[self.current_state]:
            yield self.objects[i]
        return

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.window, (SCREEN_W, SCREEN_H)), (0, 0))


class GameMenu(Scene):
    def __init__(self, input_manager):
        super().__init__(input_manager)
        self.window = pygame.Surface((SCREEN_W, SCREEN_H))
        self.background = pygame.transform.scale(
            pygame.image.load("Images/Menu/MenuAmsterdamOne.png").convert_alpha(),
            (SCREEN_W, SCREEN_H)
        )
        self.objects = [
            button_by_center('Play', SCREEN_W//2, 0.9 * SCREEN_H, 85, 50,
                             cmd=(SWITCH_STATE, [1])),
            Button('Exit', 20, 12, 80, 50,
                   cmd=(EXIT_GAME, [])),
            Button('', SCREEN_W-65, 12, 45, 45,
                   image="Images/SettingsIcon.png", cmd=(SWITCH_STATE, [2])),
            button_by_center('Winter', 0.13*SCREEN_W, SCREEN_H-60, 110, 50,
                             cmd=(SWITCH_SCENE, [1])),
            button_by_center('Summer', 0.39*SCREEN_W, SCREEN_H-60, 130, 50,
                             cmd=(SWITCH_SCENE, [2])),
            button_by_center('Spring', 0.65*SCREEN_W, SCREEN_H-60, 110, 50,
                             cmd=(SWITCH_SCENE, [3])),
            button_by_center('Fall', .91*SCREEN_W, SCREEN_H-60, 80, 50,
                             cmd=(SWITCH_SCENE, [4])),
        ]

        self.states = [
            [0],
            [1, 2, 3, 4, 5, 6],
            [0]
        ]

        self.current_state = 0

    def update(self, dt=0):
        cmd_type, param = DO_NOTHING, []
        self.window.blit(self.background, (0, 0))
        for button in self.get_active_objects():
            button.draw(self.window)
            if button.is_clicked():
                pass
                cmd_type, param = button.cmd

        if cmd_type == SWITCH_STATE:
            self.current_state = param[0]
        elif cmd_type == SWITCH_SCENE:
            return SWITCH_SCENE, [1]
        elif cmd_type == EXIT_GAME:
            return EXIT_GAME, []
        return DO_NOTHING, []

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.window, (SCREEN_W, SCREEN_H)), (0, 0))


class GameScene(Scene):
    def __init__(self, i, input_manager):
        super().__init__(input_manager)
        self.PLAYER_SPEED = 160

        self.window = pygame.Surface((SCREEN_W, SCREEN_H))
        self.current_state = 0

        self.player = Player(Vector(0, 200), self.PLAYER_SPEED, self.input_manager)
        self.camera = Camera((SCREEN_W, SCREEN_H))

        self.background_x = 0

        self.active = False
        match i:
            case 0:
                self.background = pygame.image.load("Images/Backgrounds/WinterBG.jpg").convert_alpha()
                self.background_xmax = self.background.get_size()[0]
                self.objects = level_saver.list_of_elements(
                    level_saver.load_level("levels/Winter/content.csv"),
                    self.PLAYER_SPEED
                )
                pygame.mixer.music.load("Musics/winter.ogg")

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
        if self.current_state == 1:
            return DO_NOTHING, []
        self.background_x = (self.background_x - 2) % self.background_xmax - self.background_xmax

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
                    pygame.mixer.music.stop()
                    self.active = False
        self.objects = self.objects[removed:]
        self.player.grounded = (self.player.velocity.y == 0)

        return DO_NOTHING, []

    def draw(self, screen):
        if not self.active:
            return
        self.window.blit(self.background, (self.background_x, 0))
        self.window.blit(self.background, (self.background_x+self.background_xmax, 0))
        # self.window.blit(self.background, (self.background_x+2*self.background_xmax, 0))

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

        if self.current_state == 1:
            s = pygame.Surface((SCREEN_W, SCREEN_H))
            s.set_alpha(200)
            self.window.blit(s, (0, 0))

        screen.blit(pygame.transform.scale(self.window, screen.get_size()), (0, 0))
