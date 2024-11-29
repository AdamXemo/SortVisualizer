import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def draw_element(index, value):
    margin = 10
    width = 10
    height_scale = 10
    pygame.draw.rect(screen,
                     (200, 200, 200),
                     pygame.Rect(
                        margin + index*(width+margin),
                        height - margin - height_scale*value,
                        width,
                        height_scale * value))


def draw_array(array):
    for i in range(len(array)):
        draw_element(i, array[i])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    draw_array([3,1,4,1,5])

    pygame.display.flip()
    clock.tick(60)
