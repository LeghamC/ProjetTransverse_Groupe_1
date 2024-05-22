# -------------------------------------------------------------------------------
# Name:        Aux Quatres Temps
# Author:      Lélia - Dali - Meïssa - Manon - Mathis
# Purpose:     Project's menu - the gameplay window
# Created:     01/02/2024
# -------------------------------------------------------------------------------

import pygame
import math
from sys import exit
from Physics import Vector, make_vector_polar
import Level_saver
import Collisions
import Constants
from Player import Player
from InputManager import InputManager
from Obstacle import Obstacle


def GAME():
    # CONSTANTS
    PLAYER_SPEED = 160
    FPS = 60

    # Initialization of pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((constants.SCREEN_W, constants.SCREEN_H))
    pygame.display.set_caption("Aux Quatres Temps")
    clock = pygame.time.Clock()
    font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 30)
    dt = clock.tick(FPS) * 0.001
    active = True

    # Will keep record of the inputs
    # Each Object that needs info about inputs to receive will keep a reference to that object
    input_manager = InputManager()

    # Load images and create surfaces
    background_1 = pygame.image.load("Images/Backgrounds/WinterBG.jpg").convert_alpha()
    background_xpos = 0
    background_xpos2 = 612
    background_xpos3 = 1224

    text_score = font.render("Rings 000", True, "gold")
    score_rect = text_score.get_rect(topright=(1215, 10))

    text_timer = font.render("Timer 00.00", True, "white")
    timer_rect = text_timer.get_rect(topright=(1215, 50))

    player = Player(Vector(0, 420), PLAYER_SPEED, input_manager)
    player_group = pygame.sprite.GroupSingle(player)

    game_over_text = font.render("GAME OVER", True, "black")
    game_over_rect = game_over_text.get_rect(center=(612, 230))

    # LOADING LEVEL
    level_content = level_saver.load_level("levels/Winter/content.csv")
    platforms = level_saver.list_of_elements(level_content, PLAYER_SPEED)
    platforms_group = pygame.sprite.Group(platforms)
    pygame.mixer.music.load("Musics/winter.ogg")
    pygame.mixer.music.play()

    # CAMERA
    camera = scrolling.Camera((constants.SCREEN_W, constants.SCREEN_H))

    # obstacle = Obstacle(Vector(500, 200), 50, 100)
    obstacles = pygame.sprite.Group()

    # Loop to keep the window open
    while True:
        input_manager.update(pygame.event.get())
        if input_manager.QUIT:
            pygame.quit()
            exit()

        if active:
            window.blit(background_1, (background_xpos, 0))
            window.blit(background_1, (background_xpos2, 0))
            window.blit(background_1, (background_xpos3, 0))
            window.blit(text_score, score_rect)
            window.blit(text_timer, timer_rect)

            player.update(dt)
            if player.rect.bottom >= constants.SCREEN_H:
                player.velocity.y = 0
                player.position.y = constants.SCREEN_H - player.rect.height
                player.rect.bottom = constants.SCREEN_H

            camera.update_position(player.rect)
            for element in platforms:
                camera.render_element(
                    pygame.Surface((element.rect.w, element.rect.h)),
                    element.rect,
                    window
                )

            for element in obstacles:
                camera.render_element(
                    pygame.Surface((element.rect.w, element.rect.h)),
                    element.rect,
                    window
                )

            background_xpos -= 2
            background_xpos2 -= 2
            background_xpos3 -= 2
            if background_xpos == -612:
                background_xpos = 0
                background_xpos2 = 612
                background_xpos3 = 1224

            if player.arrow.aiming:
                # Draw the arrow
                camera.render_element(
                    player.arrow.rotated_image,
                    player.arrow.rect,
                    window
                )

            # Collision detection
            for element in platforms:
                if element.rect.x > player.rect.right:
                    break
                if player.rect.colliderect(element.rect.move(0, -1)):
                    if collisions.top_collision(player.rect, element.rect.move(0, -1)):
                        player.position.y = element.rect.top - player.rect.height
                        player.rect.bottom = element.rect.top
                        player.velocity.x = PLAYER_SPEED
                        player.velocity.y = 0
                    else:
                        pygame.mixer.music.stop()
                        active = False
            player.grounded = (player.velocity.y == 0)

            for element in obstacles:
                if player.rect.colliderect(element.rect):
                    pygame.mixer.music.stop()
                    active = False

            camera.render_element(
                player.image,
                player.rect,
                window
            )
        else:
            window.fill("red")
            window.blit(game_over_text, game_over_rect)

        pygame.display.update()
        dt = clock.tick(FPS) * 0.001
