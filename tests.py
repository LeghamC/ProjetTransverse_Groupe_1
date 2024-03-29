
# IMPORTATIONS OF MODULES
import pygame
import level_saver
import collisions
import scrolling
import constants
from sys import exit

# CONSTANTS
PLAYER_SPEED = 120
FPS = 60

# CREATION OF THE GRAPHIC WINDOW
pygame.init()
window = pygame.display.set_mode((constants.SCREEN_W, constants.SCREEN_H))
pygame.display.set_caption("Shiho<3")
clock = pygame.time.Clock()
dt = clock.tick(FPS)
active = True

# BACKGROUND_1
background_xpos = 0
background_xpos2 = 612
background_xpos3 = 1224

# PLAYER SURFACE
player_shiho = pygame.Surface((50, 50))
player_shiho.fill((0, 0, 0))
player_rect = player_shiho.get_rect(topleft=(5, 380))
player_x = 5
player_gravity = 0

# LOADING LEVEL
level_content = level_saver.load_level("levels/level_0/content.csv")
elements = level_saver.list_of_elements(level_content, PLAYER_SPEED)
pygame.mixer.music.load("levels/level_0/music.mid")
pygame.mixer.music.play()

# CAMERA
camera_x = 0

# Loop to keep the window open
while True:
    for event in pygame.event.get():
        # Cross to escape window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.top >= 0:
                # If space key pressed than jump
                player_gravity = -15
    if active:
        window.fill((255, 255, 255))

        # Gravity of player's jumps
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 461:
            player_rect.bottom = 460

        # Player moving from left to right
        player_x += PLAYER_SPEED * dt * 0.001
        player_rect.right = player_x

        camera_x = scrolling.update_camera_pos(camera_x, player_rect)
        for element in elements:
            scrolling.camera_render(
                pygame.Surface((element.w, element.h)),
                element,
                window,
                camera_x
            )

        # ANIMATION
        # Background moving from right to left
        background_xpos -= 2
        background_xpos2 -= 2
        background_xpos3 -= 2
        if background_xpos == -612:
            background_xpos = 0
            background_xpos2 = 612
            background_xpos3 = 1224

        # MOUSE FUNCTIONING
        # Display of mouse cursor
        mouse_pos = pygame.mouse.get_pos()

        # COLLISION DETECTION
        for element in elements:
            if element.x > player_rect.right:
                break
            if player_rect.colliderect(element):
                if collisions.top_collision(player_rect, element):
                    player_rect.bottom = element.top
                    player_gravity = 0
                else:
                    pygame.mixer.music.stop()
                    active = False

        if player_rect.collidepoint(mouse_pos):
            print("Collision cursor")

        scrolling.camera_render(
            player_shiho,
            player_rect,
            window,
            camera_x
        )

    else:
        window.fill("Red")

    pygame.display.update()
    # Rate of 60 images per second so that the game
    # does not run too fast or too slow
    dt = clock.tick(FPS)
