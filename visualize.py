import pygame
import random
import sort
import numpy as np
import time
import pygame_menu

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1)
pygame.init()

MARGIN = 10
BAR_WIDTH = 10
HEIGHT_SCALE = 10
FPS = 60
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (200, 30, 30)
GREEN = (30, 200, 30)
BLUE = (30, 30, 200)

clock = pygame.time.Clock()

def draw_element(screen, array, index, color, height):
    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(
            MARGIN + index * (BAR_WIDTH + MARGIN),
            height - MARGIN - HEIGHT_SCALE * array[index],
            BAR_WIDTH,
            HEIGHT_SCALE * array[index]
        )
    )


def play_sine_wave(frequency):
    samples = 0.05 * np.sin(2 * np.pi * frequency * np.arange(0, 1/FPS, 1/44100))
    samples = samples.astype(np.float16)
    sound = pygame.mixer.Sound(samples)
    sound.play(0)


def draw_array(screen, array, highligh_color, play_sounds, height):
    screen.fill((0, 0, 0))
    for i in range(len(array["values"])):
        draw_element(screen, array["values"], i, GRAY, height)
    for i in array["highlight"]:
        draw_element(screen, array["values"], i, highligh_color, height)

    last_highlighted = array["values"][array["highlight"][-1]]

    if play_sounds:
        frequency = 220 * 4**((last_highlighted-1) / len(array))
        play_sine_wave(frequency)

def draw_text(screen, text, width, height):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render(text, True, WHITE)
    x = (width - text.get_width()) // 2
    y = height * 0.05
    screen.blit(text, (x, y))

def visualize_sorting(array_size, array_type, selected_algorithm):
    width = MARGIN + array_size * (BAR_WIDTH + MARGIN)
    height = 2 * MARGIN + array_size * HEIGHT_SCALE

    screen = pygame.display.set_mode((width, height))

    if array_type == "random":
        array = random.sample(range(1, array_size + 1), array_size)
    elif array_type == "reverse":
        array = list(range(array_size, 0, -1))
    elif array_type == "sorted":
        array = list(range(1, array_size + 1))
    elif array_type == "nearly":
        array = list(range(1, array_size + 1))
        for _ in range(array_size // random.randrange(5, 15)):
            idx1, idx2 = random.sample(range(array_size), 2)
            array[idx1], array[idx2] = array[idx2], array[idx1]

    algorithm_map = {
        "Bubble Sort": sort.bubble_sort,
        "Insertion Sort": sort.insertion_sort,
        "Merge Sort": sort.merge_sort,
    }

    sorting_algorithm = algorithm_map[selected_algorithm]

    paused = False
    sorting_steps = list(sorting_algorithm(array))
    current_step_index = 0
    highlighted_index = 1
    play_sounds = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play_sounds = paused
                    paused = not paused
                if event.key == pygame.K_RIGHT:  # step forward
                    if current_step_index < len(sorting_steps) - 1:
                        current_step_index += 1
                if event.key == pygame.K_LEFT:  # step backward
                    if current_step_index > 0:
                        current_step_index -= 1
                if event.key == pygame.K_r:
                    menu()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if current_step_index < len(sorting_steps) - 1:
                current_step_index += 1
        if keys[pygame.K_a]:
            if current_step_index > 0:
                current_step_index -= 1

        if not paused and current_step_index < len(sorting_steps) - 1:
            current_step_index += 1

        if current_step_index == len(sorting_steps) - 1:
            if highlighted_index < len(array) - 1:
                highlighted_index += 1
                time.sleep(0.01)
            draw_array(screen, {"values": sorting_steps[current_step_index]["values"], "highlight": [highlighted_index]}, GREEN, play_sounds, height)

            if highlighted_index == len(array) - 1:
                play_sounds = False
                draw_array(screen, {"values": sorting_steps[current_step_index]["values"], "highlight": [highlighted_index]}, GRAY, play_sounds, height)
                draw_text(screen, "Sorting Complete! Press R to Reset, Q to quit.", width, height)
        else:
            draw_array(screen, sorting_steps[current_step_index], RED, play_sounds, height)

        if paused:
            draw_text(screen, "Sorting Paused. Press Space to Resume.", width, height)

        pygame.display.flip()
        clock.tick(FPS)


def menu():
    pygame.display.set_mode((800, 600))

    custom_theme = pygame_menu.Theme(
        background_color=(0, 0, 0),
        title_font=pygame_menu.font.FONT_OPEN_SANS_BOLD,
        title_font_size=40,
        title_font_color=WHITE,
        widget_font=pygame_menu.font.FONT_OPEN_SANS,
        widget_font_color=WHITE,
        widget_font_size=24,
        widget_margin=(0, 15),
        widget_selection_effect=pygame_menu.widgets.HighlightSelection()
    )

    menu = pygame_menu.Menu('Sorting Visualizer', 800, 600, theme=custom_theme)

    array_size = menu.add.range_slider("Array Size", default=50, range_values=(10, 100), increment=10)

    array_type = menu.add.selector(
        "Array Type: ",
        [("Random", "random"), ("Reverse Sorted", "reverse"), ("Sorted", "sorted"), ("Nearly Sorted", "nearly")],
        default=0
    )

    algorithm = menu.add.selector(
        "Algorithm: ",
        [("Bubble Sort", "Bubble Sort"), ("Insertion Sort", "Insertion Sort"), ("Merge Sort", "Merge Sort")],
        default=2
    )

    menu.add.button('Start', lambda: visualize_sorting(int(array_size.get_value()), array_type.get_value()[0][1], algorithm.get_value()[0][1]))
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(pygame.display.set_mode((800, 600)))

menu()