import pygame
import random
import sort

pygame.init()

WIDTH, HEIGHT = 800, 600
MARGIN = 10
BAR_WIDTH = 10
HEIGHT_SCALE = 10
FPS = 20
ARRAY_SIZE = 20

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
    screen.fill((0, 0, 0))
    for i in range(len(array)):
        draw_element(i, array[i])


random_array = random.sample(range(ARRAY_SIZE), ARRAY_SIZE)
draw_array(random_array)

for step in sort.insertion_sort(random_array):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw_array(step)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
