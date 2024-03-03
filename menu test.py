import pygame
import math
from sys import exit
from arrow import Vector, add_vectors

# Initialization of pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((1224, 420))
pygame.display.set_caption("Shiho<3")
clock = pygame.time.Clock()
font = pygame.font.Font("Font/future-timesplitters/Future TimeSplitters.otf", 30)
active = True

# Load images and create surfaces
background_1 = pygame.image.load("Images/background_night_forest.png").convert()
background_xpos = 0
background_xpos2 = 612
background_xpos3 = 1224

text_score = font.render("Rings 000", True, "gold")
score_rect = text_score.get_rect(topright=(1215, 10))

text_timer = font.render("Timer 00.00", True, "white")
timer_rect = text_timer.get_rect(topright=(1215, 50))

platform = pygame.Surface((50, 5))
platform_rect = platform.get_rect(bottomleft=(350, 220))
platform.fill("#BBDE22")

player_shiho = pygame.image.load("Images/shiho_dollF.png").convert_alpha()
player_rect = player_shiho.get_rect(bottomleft=(0, 420))
player_velocity = Vector(0, 0)  # Initial player velocity
player_gravity = Vector(0, 1)  # Gravity vector

game_over_text = font.render("GAME OVER", True, "black")
game_over_rect = game_over_text.get_rect(center=(612, 230))

arrow_image = pygame.image.load("Images/arrow_beta.png").convert_alpha()
arrow_image = pygame.transform.scale(arrow_image, (40, 20))

# Initialize aiming variables
aiming = False
arrow_angle = 0
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
                player_velocity = add_vectors(player_velocity, Vector(5 * math.cos(math.radians(arrow_angle)), -5 * math.sin(math.radians(arrow_angle))))
                player_rect.x += 10
                player_rect.y += 10
                player_rect.centerx -= 10
                player_rect.centery -= 10

                # Stop aiming and reset arrow angle
                aiming = False
                arrow_angle = 0

    if active:
        window.blit(background_1, (background_xpos, 0))
        window.blit(background_1, (background_xpos2, 0))
        window.blit(background_1, (background_xpos3, 0))
        window.blit(text_score, score_rect)
        window.blit(text_timer, timer_rect)
        window.blit(platform, platform_rect)

        player_velocity = add_vectors(player_velocity, player_gravity)
        player_rect.y += player_velocity.magnitude
        if player_rect.bottom > 420:
            player_rect.bottom = 420

        background_xpos -= 2
        background_xpos2 -= 2
        background_xpos3 -= 2
        if background_xpos == -612:
            background_xpos = 0
            background_xpos2 = 612
            background_xpos3 = 1224

        # Draw the player
        window.blit(player_shiho, player_rect)

        if aiming:
            # Update arrow position on a semicircle path to the right of the player
            arrow_x = player_rect.centerx + arrow_radius * math.cos(math.radians(arrow_angle))
            arrow_y = player_rect.centery - arrow_radius * math.sin(math.radians(arrow_angle))

            # Rotate arrow to point towards the player
            arrow_image_rotated = pygame.transform.rotate(arrow_image, arrow_angle)
            arrow_rect = arrow_image_rotated.get_rect(center=(arrow_x, arrow_y))

            # Draw the arrow
            window.blit(arrow_image_rotated, arrow_rect)

            # Increment arrow angle for next frame
            if arrow_angle <= 85 :
                arrow_angle += 5
            if arrow_angle == 90 and arrow_angle >= 270:
                arrow_angle -=5
        # Update player position based on velocity
        if aiming:
            player_rect.x += player_velocity.magnitude * math.cos(math.radians(arrow_angle))
            player_rect.y += player_velocity.magnitude * -math.sin(math.radians(arrow_angle))

        # Collision detection
        if player_rect.colliderect(platform_rect):
            active = False
        if player_rect.collidepoint(pygame.mouse.get_pos()):
            print("Collision cursor")

    else:
        window.fill("red")
        window.blit(game_over_text, game_over_rect)

    pygame.display.update()
    clock.tick(60)