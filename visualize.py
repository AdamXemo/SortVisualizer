import pygame
import random
import sort
import numpy as np
import time

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1)
pygame.init()

MARGIN = 10
BAR_WIDTH = 10
HEIGHT_SCALE = 10
FPS = 60
ARRAY_SIZE = 50
WIDTH = MARGIN + ARRAY_SIZE*(BAR_WIDTH+MARGIN)
HEIGHT = 2*MARGIN + ARRAY_SIZE*HEIGHT_SCALE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def draw_element(array, index, color):
    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(
            MARGIN + index * (BAR_WIDTH + MARGIN),  # X position
            HEIGHT - MARGIN - HEIGHT_SCALE * array[index],  # Y position
            BAR_WIDTH,  # Bar width
            HEIGHT_SCALE * array[index]  # Bar height based on value
        )
    )


def play_sine_wave(frequency):
    samples = 0.05 * np.sin(2 * np.pi * frequency * np.arange(0, 1/FPS, 1/44100))
    samples = samples.astype(np.float16)
    sound = pygame.mixer.Sound(samples)
    sound.play(0)


def draw_array(array):
    screen.fill((0, 0, 0))
    for i in range(len(array["values"])):
        draw_element(array["values"], i, (200, 200, 200))
    for i in array["highlight"]:
        draw_element(array["values"], i, (200, 30, 30))

    last_highlighted = array["values"][array["highlight"][-1]]
    frequency = 220 * 4**((last_highlighted-1) / ARRAY_SIZE)
    play_sine_wave(frequency)

def draw_text(text):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (WIDTH // 6, HEIGHT * 0.05))


random_array = random.sample(range(1, ARRAY_SIZE+1), ARRAY_SIZE)

paused = False
sorting_steps = list(sort.bubble_sort(random_array))
current_step_index = 0
highlighted_index = 1

while True:
    redraw = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_RIGHT:  # step forward
                if current_step_index < len(sorting_steps) - 1:
                    current_step_index += 1
                    redraw = True
            if event.key == pygame.K_LEFT:  # step backward
                if current_step_index > 0:
                    current_step_index -= 1
                    redraw = True
            if event.key == pygame.K_r:
                random_array = random.sample(range(1, ARRAY_SIZE+1), ARRAY_SIZE)
                sorting_steps = list(sort.bubble_sort(random_array))
                current_step_index = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if current_step_index < len(sorting_steps) - 1:
            current_step_index += 1
            redraw = True
    if keys[pygame.K_a]:
        if current_step_index > 0:
            current_step_index -= 1
            redraw = True

    if not paused and current_step_index < len(sorting_steps) - 1:
        current_step_index += 1
        redraw = True

    if current_step_index == len(sorting_steps) - 1:
        if highlighted_index < len(random_array) - 1:
            highlighted_index += 1
            time.sleep(0.01)
        draw_array({"values": sorting_steps[current_step_index]["values"], "highlight": [highlighted_index]})

        if highlighted_index == len(random_array) - 1:
            draw_text("Sorting Complete! Press R to Reset.")
    elif redraw:
        draw_array(sorting_steps[current_step_index])

    if paused:
        draw_text("Sorting Paused. Press Space to Resume.")

    pygame.display.flip()
    clock.tick(FPS)
