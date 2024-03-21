import pygame
import math
from sys import exit
from physics import Vector, make_vector_polar
import level_saver
import collisions
import scrolling
import constants


# CONSTANTS
PLAYER_SPEED = 120
FPS = 60


# Initialization of pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((constants.SCREEN_W, constants.SCREEN_H))
pygame.display.set_caption("Shiho<3")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/VeganStylePersonalUse-5Y58.ttf", 30)
dt = clock.tick(FPS) * 0.001
active = True

# Load images and create surfaces
background_1 = pygame.image.load("Images/Backgrounds/background_night_forest.png").convert()
background_xpos = 0
background_xpos2 = 612
background_xpos3 = 1224

text_score = font.render("Rings 000", True, "gold")
score_rect = text_score.get_rect(topright=(1215, 10))

text_timer = font.render("Timer 00.00", True, "white")
timer_rect = text_timer.get_rect(topright=(1215, 50))

player_shiho = pygame.Surface((50, 50))
player_rect = player_shiho.get_rect(bottomleft=(0, 420))
player_position = Vector(0, 420)
player_velocity = Vector(PLAYER_SPEED, 0)  # Initial player velocity
player_acceleration = Vector(0, 150)  # Gravity vector

game_over_text = font.render("GAME OVER", True, "black")
game_over_rect = game_over_text.get_rect(center=(612, 230))

arrow_image = pygame.image.load("Images/arrow_beta.png").convert_alpha()
arrow_image = pygame.transform.scale(arrow_image, (40, 20))

# LOADING LEVEL
level_content = level_saver.load_level("levels/level_0/content.csv")
elements = level_saver.list_of_elements(level_content, PLAYER_SPEED)
pygame.mixer.music.load("levels/level_0/music.mid")
pygame.mixer.music.play()

# CAMERA
camera_x = 0

# Initialize aiming variables
aiming = False
arrow_angle = -90
direction = 1  # 1 for clockwise, -1 for counter-clockwise
arrow_radius = 50  # Distance from player

# Loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.top >= 0:
                # Player starts aiming when space bar is held down
                aiming = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # Player is shot in the direction of the arrow when space bar is released
                player_velocity.y += make_vector_polar(200, -arrow_angle).y
                print(player_velocity)

                # Stop aiming and reset arrow angle
                aiming = False
                arrow_angle = -90

    if active:
        window.blit(background_1, (background_xpos, 0))
        window.blit(background_1, (background_xpos2, 0))
        window.blit(background_1, (background_xpos3, 0))
        window.blit(text_score, score_rect)
        window.blit(text_timer, timer_rect)

        camera_x = scrolling.update_camera_pos(camera_x, player_rect)
        for element in elements:
            scrolling.camera_render(
                pygame.Surface((element.w, element.h)),
                element,
                window,
                camera_x
            )

        player_velocity += player_acceleration * dt
        player_position += player_velocity * dt
        player_rect.y = player_position.y
        player_rect.x = player_position.x
        if player_rect.bottom > constants.SCREEN_H:
            player_velocity = Vector(PLAYER_SPEED, 0)
            player_position.y = constants.SCREEN_H - 50
            player_rect.bottom = constants.SCREEN_H

        background_xpos -= 2
        background_xpos2 -= 2
        background_xpos3 -= 2
        if background_xpos == -612:
            background_xpos = 0
            background_xpos2 = 612
            background_xpos3 = 1224

        if aiming:
            # Update arrow position on a semicircle path to the right of the player
            arrow_x = player_rect.centerx + arrow_radius * math.cos(math.radians(arrow_angle))
            arrow_y = player_rect.centery - arrow_radius * math.sin(math.radians(arrow_angle))

            # Rotate arrow to point towards the player
            arrow_image_rotated = pygame.transform.rotate(arrow_image, arrow_angle)
            arrow_rect = arrow_image_rotated.get_rect(center=(arrow_x, arrow_y))

            # Draw the arrow
            scrolling.camera_render(
                arrow_image_rotated,
                arrow_rect,
                window,
                camera_x
            )

            # Increment arrow angle for next frame
            arrow_angle += 5 * direction

            # Change direction at 90 and -90 degrees
            if arrow_angle >= 90 or arrow_angle <= -90:
                direction *= -1

        # Collision detection
        for element in elements:
            if element.x > player_rect.right:
                break
            if player_rect.colliderect(element):
                if collisions.top_collision(player_rect, element):
                    player_position.y = element.top - 50
                    player_rect.bottom = element.top
                    player_velocity = Vector(PLAYER_SPEED, 0)
                else:
                    pygame.mixer.music.stop()
                    active = False

        scrolling.camera_render(
            player_shiho,
            player_rect,
            window,
            camera_x
        )
    else:
        window.fill("red")
        window.blit(game_over_text, game_over_rect)

    pygame.display.update()
    dt = clock.tick(FPS) * 0.001