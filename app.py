from config import WINDOW_WIDTH, WINDOW_HEIGHT, SCENE_WIDTH, FPS, GREY, FOV, WALLS
from boundary import Boundary, Particle
import pygame
import random
import math

# ====== GLOBAL CONSTANTS ======
CLOCK = pygame.time.Clock()
BOUNDARIES = []


def create_boundaries():
    BOUNDARIES.append(Boundary(-1, -1, WINDOW_WIDTH / 2, -1))
    BOUNDARIES.append(Boundary(-1, -1, -1, WINDOW_HEIGHT))
    BOUNDARIES.append(Boundary(-1, WINDOW_HEIGHT, WINDOW_WIDTH / 2, WINDOW_HEIGHT))
    BOUNDARIES.append(Boundary(WINDOW_WIDTH / 2, -1, WINDOW_WIDTH / 2, WINDOW_HEIGHT))

    for i in range(WALLS):
        x1 = random.randint(0, WINDOW_WIDTH / 2)
        y1 = random.randint(0, WINDOW_HEIGHT)
        x2 = random.randint(0, WINDOW_WIDTH / 2)
        y2 = random.randint(0, WINDOW_HEIGHT)
        BOUNDARIES.append(Boundary(x1, y1, x2, y2)) 


def user_input(user):
    keys = pygame.key.get_pressed()
    current_x = user.pos.x
    current_y = user.pos.y
    delta_X = 0
    delta_Y = 0
    if keys[pygame.K_w]:
        delta_Y -= 5
    if keys[pygame.K_s]:
        delta_Y += 5
    if keys[pygame.K_a]:
        delta_X -= 5
    if keys[pygame.K_d]:
        delta_X += 5
    current_x += delta_X
    current_y += delta_Y
    if not (current_x > SCENE_WIDTH or current_x < 0):
        user.pos.x = current_x
    if not (current_y > WINDOW_HEIGHT or current_y < 0):
        user.pos.y = current_y

    
    if keys[pygame.K_LEFT]:
        user.rotate(-0.05)
    if keys[pygame.K_RIGHT]:
        user.rotate(0.05)


def draw_window(window, particle):
    window.fill(GREY)
    particle.draw(window)
    for boundary in BOUNDARIES:
        boundary.draw(window)
    scene = particle.look(window, BOUNDARIES)

    slice_width = SCENE_WIDTH / len(scene)
    x_position = 0
    for slice in scene:
        if slice is math.inf:
            slice = SCENE_WIDTH
        slice_height = WINDOW_HEIGHT * FOV / slice
        rgb_value = abs(256 - slice * 255 / SCENE_WIDTH)

        if rgb_value > 255:
            rgb_value = 255
        pygame.draw.rect(window, (rgb_value, rgb_value, rgb_value), (SCENE_WIDTH + x_position * slice_width, WINDOW_HEIGHT / 2 - slice_height / 2, slice_width + 1, slice_height))
        x_position += 1

    pygame.display.update()


def setup():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    user = Particle()
    create_boundaries()

    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(window, user)
        user_input(user)


if __name__ == "__main__":
    setup()