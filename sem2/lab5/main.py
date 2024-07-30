import pygame
import sys


def alien_coord():
    global x_al, x_plus, y_al, alien
    x_al += x_plus
    if x_al == 400:
        x_plus = -x_plus
    elif x_al == -400:
        x_plus = -x_plus

    y_al = x_al ** 2 // 500

    return x_al + WIDTH / 2 - alien.get_width() // 10, y_al + HEIGHT / 2 - alien.get_height() // 10


def plate_coord():
    global plate_x, plate_plus, plate
    plate_x += plate_plus
    if plate_x == 480:
        plate_plus = -plate_plus
    elif plate_x == -480:
        plate_plus = -plate_plus

    return plate_x + WIDTH / 2 - 250 // 4 - 100, HEIGHT / 2 - 300


# Глобальные константы
WIDTH = 1200
HEIGHT = 700
FPS = 30

# Инициализируем все необходимые для окна параметры
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

space = pygame.image.load("pict/space.png")
space_rect = space.get_rect(bottomright=(WIDTH, HEIGHT))

alien = pygame.image.load("pict/alien.png")
alien_cor = pygame.transform.scale(alien, (alien.get_width() // 5, alien.get_height() // 5))

plate = pygame.image.load("pict/home.png")
plate = pygame.transform.scale(plate, (plate.get_width() // 2, plate.get_height() // 2))

# pygame.display.update()
x_al = y_al = 0
x_plus = 4
degrees = 0
plate_x = 0
plate_plus = 2
while True:
    screen.blit(space, space_rect)
    screen.blit(alien_cor, alien_coord())
    plate_2 = pygame.transform.rotate(plate, degrees)
    screen.blit(plate_2, plate_coord())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    degrees = (degrees + 2) % 360
    pygame.display.flip()
    clock.tick(FPS)
