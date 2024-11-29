import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
MARGIN = 10
BAR_WIDTH = 10
HEIGHT_SCALE = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def draw_element(index, value):
    pygame.draw.rect(
        screen,
        (200, 200, 200),
        pygame.Rect(
            MARGIN + index * (BAR_WIDTH + MARGIN),  # X position
            HEIGHT - MARGIN - HEIGHT_SCALE * value,  # Y position
            BAR_WIDTH,  # Bar width
            HEIGHT_SCALE * value  # Bar height based on value
        )
    )


def draw_array(array):
    for i in range(len(array)):
        draw_element(i, array[i])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    random_array = random.sample(range(50), 50)
    draw_array(random_array)

    pygame.display.flip()
    clock.tick(60)
